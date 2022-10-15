import pyautogui, random, time, cv2
import numpy as np

from src.utils.settings import *
from src.utils.bank import depositAllItems, exitBank
from src.utils.detection import imageToText, imageRectSingle, inventCount, skillLevelUp
from src.utils.colorDetection import findObject
from src.utils.window import actionImage
from src.utils.breaks import randomBreaks, _randomBreak, timer
from src.utils.support import spaces, dropItem, releaseDropItem, moveToClick, pointNorth, logMsg


j = 0
timerBreak = timer()
iBreak = random.randrange(300, 600)


def randomizer(timerBreaks, iBreaks):
    global timerBreak, iBreak
    if _randomBreak(timerBreaks, iBreaks):
        timerBreak = timer()
        iBreak = random.randrange(300, 600)


def countLogs(type):
    return inventCount(f'{type}.png')


def countNests():
    return inventCount('birdNest.png')


def doBanking():
    global j
    logMsg(f'Depositing', True)
    depositAllItems()
    randomBreaks(1, 2)

    logMsg(f'Exited Bank', True)
    exitBank()
    randomBreaks(1, 2)
    logMsg(f'Banked {j + 1} times', True)
    j += 1


def dropWood(type):
    global j
    logMsg(f'Dropping...', True)
    inventCrop()
    dropItem()
    imageRectSingle(f'{type}.png', 5, 5, 0.9, 'left', 10, 10, 40)
    releaseDropItem()
    logMsg(f'Finished Dropping! Dropped {j + 1} times', True)
    j += 1


def powerWoodcutting(type, logs):
    global timerBreak, iBreak
    while True:
        randomizer(timerBreak, iBreak)
        log = countLogs(logs)
        nest = countNests()

        inventory = log + nest
        logMsg(f'Inventory: {inventory}', True)

        if inventory > 27:
            # pointNorth()
            randomBreaks(0.5, 1)
            logMsg(f'Finding Bank', True)
            findObject(4)

            randomBreaks(9, 10)
            # dropWood(logs)
            logMsg(f'Banking {logs}', True)
            doBanking()


        actionImage()
        status = imageToText('thresh', f'{TEMP}actionScaled.png')
        text = status.strip('~-—')
        logMsg(f'Action Read: {text}', True)

        if text.lower() != 'woodcutting':
            logMsg(f'{text.lower()} matched woodcutting', True)
            findObject(type)
            logMsg(f'Finding Tree', True)
            randomBreaks(6, 9)

        if skillLevelUp() != 0:
            logMsg(f'Level up', True)
            spaces(2)

