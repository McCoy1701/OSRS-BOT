import pyautogui, random, time, cv2
import numpy as np

from src.utils.settings import *
from src.utils.bank import depositAllItems, exitBank
from src.utils.detection import imageToText, imageRectClicker, inventCount, skillLevelUp
from src.utils.colorDetection import findObject
from src.utils.window import workAreaImage, actionImage, inventCrop
from src.utils.breaks import randomBreaks, _randomBreak, timer
from src.utils.support import spaces, dropItem, releaseDropItem, moveToClick, pointNorth


j = 0


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


def doBanking():
    global j
    depositAllItems()
    randomBreaks(1, 2)

    exitBank()
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

