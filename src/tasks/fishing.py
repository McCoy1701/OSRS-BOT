import pyautogui, random, time, cv2
import numpy as np

from ..utils.detection import imageToText, imageRectClicker, inventCount, imageCount
from ..utils.screen import workAreaImage, resizeImage, inventCrop
from ..utils.breaks import randomBreaks, randomizer
from ..utils.support import spaces, dropItem, releaseDropItem, moveToClick
from ..utils.settings import *

j = 0

def dropFish(type):
    global j
    print(f'Dropping...')
    inventCrop()
    dropItem()
    imageRectClicker(f'{type}.png', 5, 5, 0.9, 'left', 10)
    releaseDropItem()
    j += 1
    print(f'Finished Dropping! Dropped {j} times')

def countFish(type):
    return inventCount(type + '.png')

def countSeaPuzzle():
    return imageCount('seaPuzzle.png')

def pickFishingSpot(type, deep = 20, cropX = 150, cropY = 150):
    workAreaImage()
    image = cv2.imread('images/workArea.png')

    objectList = [RED, GREEN, PICKUP_HIGHLIGHT, ATTACK_BLUE, YELLOW]
    boundaries = [objectList[type]]

    # print(objectList[type])
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype='uint8')
        upper = np.array(upper, dtype='uint8')
        mask = cv2.inRange(image, lower, upper)
        # output = cv2.bitwise_and(image, image, mask = mask)
        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)

        halfW = max(round(w / 2), 1)
        halfH = max(round(h / 2), 1)
        x = random.randrange(x + halfW - deep, x + max(halfW + deep, 1)) + cropX
        y = random.randrange(y + halfH - deep, y + max(halfH + deep, 1)) + cropY
        moveToClick(x, y, (0.05, 0.1), (0.01, 0.05))

    # cv2.imshow('image', np.hstack([image, output]))
    # cv2.waitKey(0)

def powerFisher(type, spot):
    while True:
        randomizer(timerBreak, iBreak)
        resizeImage()

        if type == 'prawn' or type == 'lobster':
            inv = 23
        else:
            inv = 24

        fish = countFish(type)
        puzzle = countSeaPuzzle()
        inventory = fish + puzzle
        # print(f'Fish: {inventory}')
        randomBreaks(0.2, 0.3)

        if inventory > inv:
            randomBreaks(0.2, 0.7)
            dropFish(type)
            randomBreaks(0.2, 0.7)

        fishing = imageToText('thresh', 'images/textshot.png')
        # print(f'{fishing}')

        if fishing.lower() != 'fishing':
            randomBreaks(0.2, 3)
            pickFishingSpot(spot, 10)
            randomBreaks(0.1, 3)
            skillLevelUp()

        if skillLevelUp() !=0:
            randomBreaks(0.2, 2)
            pyautogui.press('space')
            randomBreaks(0.1, 2)
            pyautogui.press('space')
            a = random.randrange(0, 2)
            spaces(a)
