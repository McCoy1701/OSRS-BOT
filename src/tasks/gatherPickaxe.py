import pyautogui, random

from utils.settings import *
from utils.bank import depositSecondItem, exitBank
from utils.detection import imageToText, isImageInRect, inventCount, skillLevelUp
from utils.colorDetection import findObject
from utils.window import screenshotWin
from utils.breaks import randomBreaks, _randomBreak, timer
from utils.support import spaces, moveToClick, pressKey, toggleRun, logMsg, dropItem, releaseDropItem, moveToWithVar


def randomizer(timerBreaks, iBreaks):
    global timerBreak, iBreak
    if _randomBreak(timerBreaks, iBreaks):
        timerBreak = timer()
        iBreak = random.randrange(300, 600)


def gatherPickaxes():
    while True:
        randomizer(timerBreak, iBreak)

        toggleRun()
        randomBreaks(0.5, 1)

        moveToWithVar(717, 176)
        logMsg('move to Mining Guild.', True)
        randomBreaks(6, 7)
        moveToWithVar(653, 201)
        logMsg('move to Mining Guild..', True)
        randomBreaks(5, 6)
        logMsg('move to Mining Guild...', True)


        randomBreaks(1, 1.5)
        logMsg('Down ladder', True)
        findObject(4)
        logMsg('Down ladder..', True)

        randomBreaks(2, 3)
        logMsg('Down ladder...', True)

        randomBreaks(4, 5)
        toggleRun()

        invo = inventCount('bronzePickaxe.png')

        while invo < 27:
            findObject(5)
            randomBreaks(10, 13)
            logMsg('Clicked on Yarsul')
            randomBreaks(1, 1.5)
            dropItem()
            moveToClick(103, 140, (0.1, 0.5), (0.01, 0.05))
            releaseDropItem()
            logMsg('Buying pickaxe', True)
            randomBreaks(0.1, 0.5)
            pyautogui.press('num1')
            logMsg('Hopping worlds', True)
            randomBreaks(15, 20)
            invo = inventCount('bronzePickaxe.png')
            logMsg(f'{invo} bronze pickaxes', True)
            if invo > 27:
                moveToClick(624, 178, (0.1, 0.5), (0.01, 0.05))
                logMsg('Moving for ladder', True)
                randomBreaks(4, 5)
                findObject(1)
                logMsg('Climbing up', True)
                randomBreaks(1, 1.5)
                moveToClick(626, 86, (0.1, 0.5), (0.01, 0.05))
                logMsg('Click bank on minimap', True)
                randomBreaks(13, 15)
                findObject(0)
                logMsg('Click bank', True)
                randomBreaks(1, 1.5)
                depositSecondItem()
                logMsg('Deposit items', True)
            invo = inventCount('bronzePickaxe.png')


timerBreak = timer()
iBreak = random.randrange(300, 600)

