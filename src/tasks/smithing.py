import pyautogui, random, time, cv2
import numpy as np

from src.utils.settings import *
from src.utils.bank import pickGold, depositSecondItem, exitBank, pickBronzeBar, pickIronBar, pickSteelBar, pickMithrilBar
from src.utils.detection import imageToText, isImageInRect, inventCount, imageCount, skillLevelUp
from src.utils.colorDetection import findObjectPrecise
from src.utils.window import screenshotWin, actionImage, inventCrop
from src.utils.breaks import randomBreaks, _randomBreak, timer
from src.utils.support import spaces, moveToClick, pressKey, toggleRun, logMsg


pickOptions = {0: pickBronzeBar, 1: pickIronBar, 2: pickSteelBar, 3: pickMithrilBar, 4: pickGold}
barList = ['bronzeBar.png', 'ironBar.png', 'steelBar.png', 'mithrilBar.png', 'goldBar.png']


def smithItems(bar, cost):
    global pickOptions, barList

    while True:
        findObjectPrecise(0)
        logMsg('finding bank', True)
        randomBreaks(1, 2)
        depositSecondItem()
        logMsg('depositing Items', True)
        randomBreaks(0.3, 1)
        pickOptions[bar]()
        logMsg('collecting Gold', True)
        randomBreaks(0.3, 0.5)
        exitBank()
        logMsg('exiting Bank', True)
        randomBreaks(0.1, 0.5)
        toggleRun()
        logMsg('disabled Running', True)

        invo = inventCount(barList[bar])

        randomBreaks(0.8, 1.2)
        findObjectPrecise(1)
        logMsg('find Furnace', True)
        randomBreaks(9, 10)
        logMsg('shitting', True)

        if isImageInRect('craftingMenu.png', screenshotWin):
            spaces(1)
            logMsg('clicked Space', True)


        while invo > cost - 1:
            if skillLevelUp() != 0:
                logMsg('level up', True)
                a = random.randrange(2, 3)
                spaces(a)
                randomBreaks(1, 2)
                findObjectPrecise(1)
                logMsg('find furnace', True)
                randomBreaks(1, 2)
                if isImageInRect('craftingMenu.png', screenshotWin):
                    spaces(1)
                    logMsg('click space', True)
            invo = inventCount(barList[bar])

        toggleRun()
        logMsg('enable running', True)
        randomBreaks(0.5, 1)
        moveToClick(610, 168, (0.1, 0.2), (0.01, 0.05))
        logMsg('move to bank', True)
        randomBreaks(6, 7)


