import pyautogui, random, time, cv2
import numpy as np

from src.utils.settings import *
from src.utils.detection import imageToText, imageRectClicker, inventCount, skillLevelUp
from src.utils.colorDetection import findObject
from src.utils.window import workAreaImage, actionImage, inventCrop
from src.utils.breaks import randomBreaks, _randomBreak
from src.utils.support import spaces, dropItem, releaseDropItem, moveToClick, pointNorth


j = 0


def timer():
    startTime = time.time()
    return startTime


def randomizer(timerBreaks, iBreaks):
    global timerBreak, iBreak
    # test = timer()
    # print(f'{iBreaks, timerBreaks} test: {test - timerBreaks} {test - timerBreaks > iBreaks}')
    if _randomBreak(timerBreaks, iBreaks):
        timerBreak = timer()
        iBreak = random.randrange(300, 600)


def countLogs(type):
    return inventCount(f'{type}.png')


def countNests():
    return inventCount('birdNest.png')


def moveDepositAll():
    bX = random.randrange(455 - 5, 455 + 5)
    bY = random.randrange(379 - 5, 379 + 5)
    moveToClick(bX, bY, (0.1, 0.3), (0.05, 0.15))


def closeButton():
    x = random.randrange(496 - 5, 496 + 5)
    y = random.randrange(87 - 5, 87 + 5)
    moveToClick(x, y, (0.1, 0.3), (0.05, 0.15))


def doBanking():
    global j
    moveDepositAll()
    randomBreaks(1, 2)

    closeButton()
    randomBreaks(1, 2)
    j += 1
    print(f'banked {j} times')


def dropWood(type):
    global j
    print(f'Dropping...')
    inventCrop()
    dropItem()
    imageRectClicker(f'{type}.png', 5, 5, 0.9, 'left', 10, 10, 40)
    releaseDropItem()
    j += 1
    print(f'Finished Dropping! Dropped {j} times')


def powerWoodcutting(type, logs):
    global timerBreak, iBreak
    while True:
        randomizer(timerBreak, iBreak)
        log = countLogs(logs)
        nest = countNests()

        inventory = log + nest
        # print(f'{inventory}')

        if inventory > 27:
            # pointNorth()
            randomBreaks(0.5, 1)
            findObject(4)

            randomBreaks(9, 10)
            # dropWood(logs)
            doBanking()


        actionImage()
        status = imageToText('thresh', f'{TEMP}actionScaled.png')
        text = status.strip('~-—')
        # print(f'{text}')

        if text.lower() != 'woodcutting':
            # print(f'{text.lower()}')
            findObject(type)
            randomBreaks(6, 9)

        if skillLevelUp() != 0:
            spaces(2)

actionImage()
timerBreak = timer()
iBreak = random.randrange(300, 600)

