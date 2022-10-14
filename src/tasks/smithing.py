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
j = 0

def randomizer(timerBreaks, iBreaks):
    global timerBreak, iBreak
    # test = timer()
    # print(f'{iBreaks, timerBreaks} test: {test - timerBreaks} {test - timerBreaks > iBreaks}')
    if _randomBreak(timerBreaks, iBreaks):
        timerBreak = timer()
        iBreak = random.randrange(300, 600)


def moveToBank(a, b, vari):
    x = random.randrange(a - vari, a + vari)
    y = random.randrange(b - vari, b + vari)
    moveToClick(x, y, (0.1, 0.2), (0.01, 0.05))


def smithItems(bar, cost):
    global pickOptions, barList, j

    while True:
        randomizer(timerBreak, iBreak)
        randomBreaks(1, 5)
        logMsg('Finding Bank', True)
        findObjectPrecise(0)
        randomBreaks(1.5, 2)
        logMsg('Depositing Items', True)
        depositSecondItem()
        randomBreaks(0.3, 0.5)
        logMsg('Collecting Gold', True)
        pickOptions[bar]()
        randomBreaks(0.3, 0.5)
        logMsg('Exiting Bank', True)
        exitBank()
        randomBreaks(0.1, 0.5)
        logMsg('Disabled Running', True)
        toggleRun()

        invo = inventCount(barList[bar])

        randomBreaks(0.8, 1.2)
        logMsg('Finding Furnace', True)
        findObjectPrecise(1)
        logMsg('Moving to Furnace', True)
        randomBreaks(9, 10)

        if isImageInRect('craftingMenu.png', screenshotWin):
            logMsg('clicked Space', True)
            spaces(1)


        while invo > cost - 1:
            logMsg('Working...', True)
            if skillLevelUp() != 0:
                logMsg('level up', True)
                a = random.randrange(2, 3)
                spaces(a)
                randomBreaks(1, 2)
                findObjectPrecise(1)
                logMsg('Finding Furnace, Again', True)
                randomBreaks(1, 2)
                if isImageInRect('craftingMenu.png', screenshotWin):
                    spaces(1)
                    logMsg('Clicking Space', True)
            invo = inventCount(barList[bar])

        toggleRun()
        logMsg('Enable Running', True)
        randomBreaks(0.5, 1)
        moveToBank(606, 169, 5)
        logMsg('Moving to Bank', True)
        randomBreaks(5, 5.2)
        logMsg(f'Finished {j + 1} runs')
        j += 1


timerBreak = timer()
iBreak = random.randrange(300, 600)

