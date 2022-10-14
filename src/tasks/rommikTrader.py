import pyautogui, random

from src.utils.settings import *
from src.utils.bank import depositSecondItem, exitBank
from src.utils.detection import imageToText, isImageInRect, inventCount, skillLevelUp
from src.utils.colorDetection import findObjectPrecise
from src.utils.window import screenshotWin
from src.utils.breaks import randomBreaks, _randomBreak, timer
from src.utils.support import spaces, moveToClick, shiftClick, toggleRun, logMsg

def clickSpot(a, b):
    x = random.randrange(a - 1, a + 1)
    y = random.randrange(b - 1, b + 1)
    shiftClick(x, y)

def trader():
    while True:
        randomBreaks(0.5, 1)
        findObjectPrecise(5)
        logMsg('Finding Rommik', True)
        randomBreaks(4, 5)

        if isImageInRect('craftySupply.png', screenshotWin):

            clickSpot(291, 148)
            logMsg('Buying Needles', True)
            randomBreaks(1, 2)

            logMsg('Buying Threads', True)
            for x in range(6):
                randomBreaks(0.1, 0.2)
                clickSpot(339, 148)

            randomBreaks(1, 2)
            moveToClick(500, 110, (0.1, 0.2), (0.01, 0.05))
            logMsg('Closing Store', True)

            randomBreaks(1, 2)
            pyautogui.press('num1')
            logMsg('Hop world', True)
            randomBreaks(10, 15)

        else:
            continue

