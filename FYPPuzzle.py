import os
from flask import Flask, render_template, request
from Services import MainServices
from werkzeug.utils import secure_filename
import MainImplementation
from PIL import Image
import train
import SolutionImplementation

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = '/Users/Nikita/StegoImage/'
app.config['UPLOAD_FOLDER'] = '/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'tiff'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


trained = 0

correctWords = ['purple', 'black', 'brown', 'pink', 'yellow', 'orange', 'red', 'blue', 'green', 'white']
@app.route('/')
def index():

    MainServices.clean_dir()
    # train.trainNeuralNet()
    return render_template('index.html')


filename = None
@app.route('/upload', methods=['POST'])
def upload():
    global filename
    MainServices.clean_dir()
    filename = None
    file = request.files['file']
    if file and allowed_file(file.filename):
        # print (os.path.realpath(file.filename))
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    print("here")
    MainImplementation.cropImage()
    print("filename ---", filename)
    return render_template('retrieveM.html',message='', displayVal = False, originalFile = filename)


detected = []
@app.route('/retrieve', methods=['POST'])
def getMsg():
    global detected
    charsDetected = MainImplementation.neuralNetTrainDetect()
    k = 0

    for i in range(15):
        new = []
        for j in range(15):
            new.append(charsDetected[k])
            k = k + 1
        detected.append(new)
        print(new)
        print("#########")
        new = []
    print(detected)
    #
    # return render_template("showDetectedGrid.html", detected = detected)
    # print("rendering---")
    # return render_template("showDetectedGrid.html")

    SolutionImplementation.dictionaryProcessing()
    SolutionImplementation.getCombinationWords(detected)
    SolutionImplementation.initializeTrie()
    return render_template("showDetectedGrid.html", detected = detected, grid = False, originalFile = filename, matchedWords = [], matchedMeaning = [], matchedDirection = [], yesNoList = [])


@app.route('/solutionL', methods=['POST'])
def solutionL():
    global detected
    global filename
    print("ajshdjasd")
    matchedWords = []
    matchedMeaning = []
    matchedDirection = []
    matchedWords, matchedMeaning, matchedDirection = SolutionImplementation.LinearSearchImplementation()

    print("Using Linear", len(matchedWords))
    global correctWords
    yesNoList = []
    for item in matchedWords:
        if item  not in correctWords:
            yesNoList.append("NO")
        else:
            yesNoList.append("YES")

    return render_template("showDetectedGrid.html", detected=detected, grid = True, originalFile = filename, matchedWords = enumerate(matchedWords), matchedMeaning = matchedMeaning, matchedDirection = matchedDirection, yesNoList = yesNoList)

@app.route('/solutionB', methods=['POST'])
def solutionB():
    global detected
    global filename
    matchedWords = []
    matchedMeaning = []
    matchedDirection = []
    matchedWords, matchedMeaning, matchedDirection = SolutionImplementation.binarySearchImplementation()
    global correctWords
    yesNoList = []
    for item in matchedWords:
        if item  not in correctWords:
            yesNoList.append("NO")
        else:
            yesNoList.append("YES")

    print("Using Binary", len(matchedWords))
    return render_template("showDetectedGrid.html", detected=detected, grid=True, matchedWords = enumerate(matchedWords), matchedMeaning = matchedMeaning, matchedDirection = matchedDirection, yesNoList = yesNoList)


@app.route('/solutionT', methods=['POST'])
def solutionT():
    global detected
    global filename
    matchedWords = []
    matchedMeaning = []
    matchedDirection = []
    matchedWords, matchedMeaning, matchedDirection = SolutionImplementation.TriesImplementation()
    print("Using TR", len(matchedWords))
    global correctWords
    yesNoList = []
    for item in matchedWords:
        if item  not in correctWords:
            yesNoList.append("NO")
        else:
            yesNoList.append("YES")

    return render_template("showDetectedGrid.html", detected=detected, grid = True, matchedWords = enumerate(matchedWords), matchedMeaning = matchedMeaning, matchedDirection = matchedDirection, yesNoList = yesNoList)


# actualGrids = [['M','Z','E','W','F','L','U','T','Z','T','T','O','U','F','R'],['V','Z','M','M','E','L','F','G','C','D','D','J','M','I','G'],['C','O','Z','O','K','C','E','M','T','D','B','L','Q','Y','G'],
# ['M', 'X', 'B', 'W', 'G', 'L', 'B', 'P', 'O', 'L', 'S', 'U', 'E', 'K', 'G'],['Y','K','U','A','K','G','I','R','A','N','N','A','G','T','D'],['A','J','Q','D','G','K','G','C','E','P','Y','G','N','M','B'],
# ['R', 'C', 'V', 'G', 'Z', 'C', 'K', 'F', 'T', 'K', 'J', 'A', 'A', 'I', 'B'],['N','Q','K','F','X','O','J','A','I','I','N','Q','R','F','W'],['Q','G','Y','R','E','C','T','E','H','J','R','N','O','L','X']
#                ,['N','P','F','U','W','R','L','','','','','','','',''],['','','','','','','','','','','','','','',''],['','','','','','','','','','','','','','',''],
#                ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],['','','','','','','','','','','','','','',''],['','','','','','','','','','','','','','','']]

@app.errorhandler(Exception)
def all_exception_handler(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
