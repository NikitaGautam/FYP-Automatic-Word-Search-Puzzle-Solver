from __future__ import division
import numpy
import scipy.special
import random
import dill

from PIL import Image
from glob import glob
import cv2
from os.path import join, dirname, realpath

def cropImage():
    for image in glob("/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/*"):
        print(image)
        file_name = image
        img_final = image
        captch_ex_fs(file_name, img_final)


def captch_ex_fs(file_name, img_final):
    img = cv2.imread(file_name)
    img_final = cv2.imread(img_final)
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 0, 100, cv2.THRESH_BINARY)
    nImage = cv2.adaptiveThreshold(img2gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 75, 10)
    cv2.imwrite("/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/T.png", nImage)

    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    ret, new_img = cv2.threshold(image_final, 0, 100, cv2.THRESH_BINARY)  # for black text , cv.THRESH_BINARY_INV
    new_img = 255 - nImage
    cv2.imwrite("/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/H.png", new_img)
    # cv2.waitKey(1000)
    '''
            line  8 to 12  : Remove noisy portion
    '''
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9,
                                                         1))  # to manipulate the orientation of dilution , large x means horizonatally dilating  more, large y means vertically dilating more
    dilated = cv2.dilate(new_img, kernel, iterations=100)  # dilate , more the iteration more the dilation

    # contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # get contours
    cv2.imwrite("/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/final_dialted.png", dilated)

    image, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # cv3.x.x

    our_contours = []

    for contour in contours:
        [x, y, w, h] = cv2.boundingRect(contour)
        our_contours.append([x, y, w, h])
    our_contours.sort(key=lambda x: x[1])

    index = 0
    first_segments = [];
    for contour in our_contours:
        [x, y, w, h] = contour
        if w < 35 and h < 35:
            continue
        rec = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        cv2.imwrite("/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/segmentedCountour.png", rec)
        cropped = img2gray[y:y + h, x: x + w]
        s = 'firstseg' + str(index) + '.png'
        cv2.imwrite("/Users/Nikita/PycharmProjects/FYPPuzzle/static/Diluted/" + s, cropped)
        index = index + 1
        first_segments.append(s)
    segmentVertically()


def segmentVertically():
    mainItem = 0
    for i in range(0, 15):
        dir = "/Users/Nikita/PycharmProjects/FYPPuzzle/static/Diluted/firstseg" + str(i) + ".png"
        image = cv2.imread(dir, 0)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5, 5))
        image = clahe.apply(image)
        img_final = cv2.imread(dir)
        img2gray = cv2.cvtColor(img_final, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 40, 100, cv2.THRESH_BINARY)
        image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (1, 3))
        image_final = cv2.erode(image_final, kernel, iterations=0)

        size = (5, 5)
        image = cv2.GaussianBlur(image, size, 10)
        image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 75, 10)
        image = cv2.bitwise_not(image)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (1, 9))
        image = cv2.dilate(image, kernel, iterations=10)
        cv2.imwrite("/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/hori_dialted.png", image)

        _, contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        index = 0
        x1 = []
        y1 = []
        w1 = []
        h1 = []

        s_contour = []
        for contour in contours:
            [x, y, w, h] = cv2.boundingRect(contour)
            if w < 5 and h < 5:
                continue
            index = index + 1

            x1.append(x)
            y1.append(y)
            w1.append(w)
            h1.append(h)
            #     print(index)
        newArray = []
        newAr = list(zip(x1, y1, w1, h1))
        xnew = []
        ynew = []
        wnew = []
        hnew = []
        newArray = sorted(newAr, key=lambda k: [k[0]])

        for item in newArray:
            #         print(item)
            for index, it in enumerate(item):
                if index == 0:
                    xnew.append(it)
                if index == 1:
                    ynew.append(it)
                if index == 2:
                    wnew.append(it)
                if index == 3:
                    hnew.append(it)
        file_name = "/Users/Nikita/PycharmProjects/FYPPuzzle/static/Diluted/firstseg" + str(0) + ".png"
        newImage = cv2.imread(file_name)
        for index, item in enumerate(xnew):
            x = xnew[index]
            y = ynew[index]
            w = wnew[index]
            h = hnew[index]
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)
            rec = cv2.rectangle(newImage, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.imwrite("/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/horiContour" + str(i) + ".png", rec)
            cropped = image_final[y:y + h, x: x + w]
            cropped = cv2.resize(cropped, (28, 28))
            s = '/Users/Nikita/PycharmProjects/FYPPuzzle/static/CroppedImages/crop_' + str(mainItem) + '.png'
            cv2.imwrite(s, cropped)
            mainItem = mainItem + 1


def neuralNetTrainDetect():
    with open('/Users/Nikita/PycharmProjects/FYPPuzzle/static/nn.dill', 'rb') as f:  # load the trained Neural Network
        nn = dill.load(f)

    char_number_map = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G',
                       7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R',
                       18: 'S', 19: 'T',
                       20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}
    answer = {}
    correctList = []

    for item in range(0, 225):
        im = Image.open('/Users/Nikita/PycharmProjects/FYPPuzzle/static/CroppedImages/crop_' + str(item) + '.png')
        img_values = list(im.getdata())
        input = (numpy.asfarray(img_values[0:]) / 255 * 0.99) + 0.01
        outputs = nn.predict(input)
        print("ere")
        label = numpy.argmax(outputs)
        predictedCharacter = str(char_number_map[label])
        answer[item] = predictedCharacter
        correctList.append(predictedCharacter)
    print(len(answer))
    return correctList



