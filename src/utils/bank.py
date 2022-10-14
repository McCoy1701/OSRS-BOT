import cv2, pyautogui, random
from src.utils.support import pickItem, moveToClick
from src.utils.breaks import randomBreaks


def exitBank():
    pickItem(499, 90)
    randomBreaks(0.3, 0.7)


def depositSecondItem():
    pickItem(629, 304)
    randomBreaks(0.3, 0.7)


def depositAllItems():
    pickItem(456, 380)
    randomBreaks(0.3, 0.7)


def pickGold():
    pickItem(294, 171)
    randomBreaks(0.5, 0.7)


def pickBucket():
    pickItem(506, 307)
    randomBreaks(0.5, 1.5)


def pickBronzeBar():
    pickItem(219, 511)
    randomBreaks(0.5, 1.5)


def pickIronBar():
    pickItem(269, 516)
    randomBreaks(0.5, 1.5)


def pickSteelBar():
    pickItem(317, 517)
    randomBreaks(0.5, 1.5)


def pickMithrilBar():
    pickItem(362, 513)
    randomBreaks(0.5, 1.5)

