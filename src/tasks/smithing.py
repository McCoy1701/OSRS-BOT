import pyautogui, random, time, cv2
import numpy as np

from src.utils.detection import imageToText, imageRectSingle, inventCount, imageCount
from src.utils.colorDetection import findObject
from src.utils.window import workAreaImage, actionImage, inventCrop
from src.utils.breaks import randomBreaks, randomizer, timer
from src.utils.support import spaces, moveToClick, pressKey

j = 0


def smithItems(amount, bar, cost, item):
    i = round((amount * cost) / 27) + 1
    pickOptions = {0: pickBronzeBar, 1: pickIronBar, 2: pickSteelBar, 3: pickMithrilBar}
    barList = ['bronzeBar.png', 'ironBar.png', 'steelBar.png', 'mithrilBar.png']

    while i > 0:
        bankSpotVarrock()
        randomBreaks(7.5, 9)
        depositSecondItem()
        randomBreaks(0.3, 0.5)
        pickOptions[bar]()
        exitBank()
        randomBreaks(0.05, 0.2)
        invo = inventoryEnabled()
        if invo == 0:
            pyautogui.press('esc')
        inv = imageCount(barList[bar])
        smithSpotVarrock()
        randomBreaks(7.5, 9)
        smithObject(item + '.png')
        while inv > cost:
            if skillLevelUp() != 0:
                randomBreaks(0.2, 3)
                pyautogui.press('space')
                randomBreaks(0.1, 3)
                pyautogui.press('space')
                a = random.randrange(0, 2)
                spaces(a)
                smithSpotVarrock()
                randomBreaks(1, 2)
                smithObject(item + '.png')
            inv = imageCount(barList[bar])
        j -= 1


