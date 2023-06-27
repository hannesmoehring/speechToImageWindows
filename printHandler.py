import os

from PIL import ImageGrab, Image


def routine(timestamp):
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png')
    image = Image.open('screenshot.png')
    image.rotate(-90)
    path = 'img' + timestamp + '.png'
    image.save(os.path.join('imgOnLayout', path))
    return os.path.join('imgOnLayout', path)



def printImg(path):
    print("print print print")
    print("printing " + str(path))

    # os.startfile(path, "print")
