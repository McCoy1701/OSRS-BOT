import pyautogui, random, time, cv2
import numpy as np

from ..utils.detection import imageToText, skillLevelUp
from ..utils.colorDetection import findObject
from ..utils.window import attackImage
from ..utils.breaks import randomBreaks, randomizer, timer
from ..utils.support import spaces, logMsg
from ..utils.settings import *


def powerAttack(monster = 'chicken'):
    global timerBreak, iBreak
    logMsg('Starting...', True)
    while True:
        logMsg('randomizer', True)
        timerBreak, iBreak = randomizer(timerBreak, iBreak)
        logMsg('Reading Image', True)
        attackImage()
        status = imageToText('thresh', fr'{TEMP}attackScaled.png')
        newText = status.strip('-|—')
        logMsg(f'Read: {newText}', True)

        if newText.lower() != monster:
            logMsg(f'Came Through: {newText}', True)
            findObject(4, True)
            logMsg(f'Finding {monster}', True)
            randomBreaks(6, 8)

            if skillLevelUp() != 0:
                logMsg(f'Level up', True)
                spaces(2)
        else:
            logMsg('Miss click', True)
            continue


attackImage()
timerBreak = timer()
iBreak = random.randrange(300, 600)

