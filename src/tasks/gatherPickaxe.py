import pyautogui

from src.utils.settings import *
from src.utils.bank import depositSecondItem, exitBank
from src.utils.detection import imageToText, isImageInRect, inventCount, skillLevelUp
from src.utils.colorDetection import findObjectPrecise
from src.utils.window import screenshotWin
from src.utils.breaks import randomBreaks, _randomBreak, timer
from src.utils.support import spaces, moveToClick, pressKey, toggleRun, logMsg, dropItem

def gatherPickaxes():
    while True:
        moveToClick(671, 205, (0.3, 0.5), (0.01, 0.05))

        randomBreaks(0.5, 1)
        toggleRun()
        logMsg('move to Mining Guild', True)

        randomBreaks(10, 13)
        findObjectPrecise(4)
        logMsg('Down ladder', True)

        randomBreaks(2, 3)
        toggleRun()

        findObjectPrecise(5)
        logMsg('Clicked on Yarsul')
        invo = inventCount('bronzePickaxe.png')

        while invo < 27:
            dropItem()
            moveToClick(103, 140, (0.1, 0.5), (0.01, 0.05))
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
                findObjectPrecise(4)
                logMsg('Moving for ladder', True)
                randomBreaks(1, 1.5)
                moveToClick(626, 86, (0.1, 0.5), (0.01, 0.05))
                randomBreaks(13, 15)
                findObjectPrecise(0)
                randomBreaks(1, 1.5)
                depositSecondItem()
            invo = inventCount('bronzePickaxe.png')






