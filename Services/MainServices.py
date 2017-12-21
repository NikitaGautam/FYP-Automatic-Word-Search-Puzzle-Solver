import os
import shutil

def clean_dir():
    shutil.rmtree("/Users/Nikita/PycharmProjects/FYPPuzzle/static/CroppedImages/")
    os.mkdir("/Users/Nikita/PycharmProjects/FYPPuzzle/static/CroppedImages/")
    shutil.rmtree("/Users/Nikita/PycharmProjects/FYPPuzzle/static/Diluted/")
    os.mkdir("/Users/Nikita/PycharmProjects/FYPPuzzle/static/Diluted/")
    shutil.rmtree("/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/")
    os.mkdir("/Users/Nikita/PycharmProjects/FYPPuzzle/static/pics/")