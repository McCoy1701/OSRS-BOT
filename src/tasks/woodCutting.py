import random

from ..utils.settings import *
from ..utils.bank import doBanking
from ..utils.detection import imageToText, imageRectSingle, inventCount, skillLevelUp
from ..utils.colorDetection import findObject
from ..utils.window import actionImage
from ..utils.breaks import _randomBreak, timer
from ..utils.support import spaces, dropItem, releaseDropItem, logMsg, randomBreaks


J = 0
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


def dropWood(type):
    global J
    logMsg(f'Dropping...', True)
    dropItem()
    imageRectSingle(f'{type}.png', 5, 5, 0.9, 'left', 10, 10, 40)
    releaseDropItem()
    logMsg(f'Finished Dropping! Dropped {j + 1} times', True)
    J += 1


def readActionImage() -> str:
    actionImage()
    status = imageToText('thresh', f'{TEMP}actionScaled.png')
    text = status.strip('~-—')
    logMsg(f'Action Read: {text}', True)
    return text


def powerWoodcutting(type, logs):
    while True:
        randomizer(timerBreak, iBreak)
        log = countLogs(logs)
        nest = countNests()

        inventory = log + nest
        logMsg(f'Inventory: {inventory}', True)

        if inventory >= 27:
            # pointNorth()
            randomBreaks(0.5, 1)
            logMsg(f'Finding Bank', True)
            findObject(0, False, 10)

            randomBreaks(9, 10)
            # dropWood(logs)
            logMsg(f'Banking {logs}', True)
            doBanking()


        text = readActionImage()

        if text.lower() != 'woodcutting':
            logMsg(f'{text.lower()} matched woodcutting', True)
            findObject(type, False, 10)
            logMsg(f'Finding Tree', True)
            randomBreaks(6, 9)

        if skillLevelUp() != 0:
            logMsg(f'Level up', True)
            spaces(2)

