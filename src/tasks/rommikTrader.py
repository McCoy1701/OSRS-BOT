import pyautogui, random

from src.utils.settings import *
from src.utils.bank import depositSecondItem, exitBank
from src.utils.detection import imageToText, isImageInRect, inventCount, skillLevelUp
from src.utils.colorDetection import findObjectPrecise
from src.utils.window import screenshotWin
from src.utils.breaks import randomBreaks, _randomBreak, timer
from src.utils.support import spaces, moveToClick, shiftClick, toggleRun, logMsg


def randomizer(timerBreaks, iBreaks):
    global timerBreak, iBreak
    # test = timer()
    # print(f'{iBreaks, timerBreaks} test: {test - timerBreaks} {test - timerBreaks > iBreaks}')
    if _randomBreak(timerBreaks, iBreaks):
        timerBreak = timer()
        iBreak = random.randrange(300, 600)


def clickSpot(a, b):
    x = random.randrange(a - 1, a + 1)
    y = random.randrange(b - 1, b + 1)
    shiftClick(x, y)


def trader():
    while True:
        randomizer(timerBreak, iBreak)
        randomBreaks(0.5, 1)
        findObjectPrecise(5)
        logMsg('Finding Rommik', True)
        randomBreaks(4, 5)

        if isImageInRect('craftySupply.png', screenshotWin):

            clickSpot(291, 148)
            logMsg('Buying Needles', True)
            randomBreaks(1, 2)

            for x in range(10):
                logMsg(f'Buying Threads {x + 1}', True)
                randomBreaks(0.1, 0.2)
                clickSpot(339, 148)

            randomBreaks(1, 2)
            moveToClick(500, 110, (0.1, 0.2), (0.01, 0.05))
            logMsg('Closing Store', True)

            randomBreaks(1, 2)
            pyautogui.press('num1')
            logMsg('Hopping worlds', True)
            randomBreaks(10, 15)

        else:
            logMsg('Miss click', True)
            continue


timerBreak = timer()
iBreak = random.randrange(300, 600)

