import pyautogui, random, time, cv2
import numpy as np

from utils.detection import imageToText, skillLevelUp
from utils.colorDetection import findObject
from utils.window import screenshotWin, attackImage
from utils.breaks import randomBreaks, _randomBreak
from utils.support import spaces, moveToClick, logMsg
from utils.settings import *

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

monsterArray = [['chicken'], ['cow'], ['guard'], ['monk']]
monsters = ['chicken', 'cow', 'guard', 'monk']

def powerAttack(monster = 'chicken'):
    while True:
        randomizer(timerBreak, iBreak)
        attackImage()
        status = imageToText('thresh', fr'{TEMP}attackScaled.png')

        if status.lower() != monster:
            # print(f'{status.lower()}')
            findObject(4)
            randomBreaks(6, 8)

            if skillLevelUp() != 0:
                spaces(2)
        else:
            logMsg('Miss click')
            continue

attackImage()
timerBreak = timer()
iBreak = random.randrange(300, 600)

