import pyautogui, random, time, cv2
import numpy as np

from src.utils.detection import imageToText, imageRectSingle, inventCount, imageCount, findObjectPrecise
from src.utils.screen import workAreaImage, resizeImage, inventCrop
from src.utils.bank import depositSecondItem, exitBank
from src.utils.breaks import randomBreaks, randomizer
from src.utils.support import spaces, pickItem

j = 0

def bankSpotEdgeVille():
    findObjectPrecise(1)

def bankSpotVarrock():
    findObjectPrecise(2)

def waterSpotEdgeVille():
    findObjectPrecise(0, 0, 0, 610, 775)

def smithSpotVarrock():
    findObjectPrecise(0, 0, 0, 610, 775)

def buckObject(type):
    imageRectSingle(type, 5, 5, 0.8, 'left', 10)

def smithObject(type):
    imageRectSingle(type, 10, 10, 0.8, 'left', 10)

# def getBuckets(item):

# def waterMoneyMaker(num, item):

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

resizeImage()
