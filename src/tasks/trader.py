import pyautogui, random

from src.utils.settings import *
from src.utils.bank import depositSecondItem
from src.utils.detection import isImageInRect, inventCount, skillLevelUp
from src.utils.colorDetection import findObject
from src.utils.window import screenshotWin
from src.utils.breaks import randomBreaks, _randomBreak, timer
from src.utils.support import shiftClick, logMsg, moveToWithVar


timerBreak = timer()
iBreak = random.randrange(300, 600)


def randomizer(timerBreaks, iBreaks):
    global timerBreak, iBreak
    if _randomBreak(timerBreaks, iBreaks):
        timerBreak = timer()
        iBreak = random.randrange(300, 600)


def threadTrader():
    while True:
        randomizer(timerBreak, iBreak)
        randomBreaks(0.5, 1)
        findObject(5)
        logMsg('Finding Rommik', True)
        randomBreaks(2, 3)

        if isImageInRect('craftySupply.png', screenshotWin):

            moveToWithVar(291, 148)
            logMsg('Buying Needles', True)
            randomBreaks(1, 2)

            for x in range(10):
                logMsg(f'Buying Threads {x + 1}', True)
                randomBreaks(0.1, 0.2)
                clickSpot(339, 148)

            randomBreaks(1, 2)
            moveToWithVar(500, 110)
            logMsg('Closing Store', True)

            randomBreaks(1, 2)
            logMsg('Hopping worlds', True)
            pyautogui.press('num1')
            randomBreaks(10, 15)

        else:
            logMsg('Miss click', True)
            continue


def eyeTrader():
    while True:
        randomizer(timerBreak, iBreak)
        randomBreaks(0.5, 1)
        findObject(5)
        logMsg('Finding Betty', True)
        randomBreaks(2, 3)

        if isImageInRect('bettyMagic.png', screenshotWin):

            moveToWithVar(437, 198)
            logMsg('Buying Eye of Newt Pack', True)

            randomBreaks(1, 2)
            moveToWithVar(500, 110)
            logMsg('Closing Store', True)

            invo = inventCount('eyeOfNewtPack.png')

            logMsg(f'Eye Of Newt Pack {invo}', True)

            if invo >= 25:
                logMsg(f'Opening packs', True)
                depositSecondItem()
                randomBreaks(26, 27)

            randomBreaks(1, 2)
            logMsg('Hopping worlds', True)
            pyautogui.press('num1')
            randomBreaks(10, 15)

        else:
            logMsg('Miss click', True)
            continue

