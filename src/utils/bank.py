import cv2, pyautogui, random
from utils.support import moveToWithVar
from utils.breaks import randomBreaks


def exitBank():
    moveToWithVar(499, 90)
    randomBreaks(0.3, 0.7)


def depositSecondItem():
    moveToWithVar(629, 304)
    randomBreaks(0.3, 0.7)


def depositAllItems():
    moveToWithVar(456, 380)
    randomBreaks(0.3, 0.7)


def pickGold():
    moveToWithVar(294, 171)
    randomBreaks(0.5, 0.7)


def pickBucket():
    moveToWithVar(506, 307)
    randomBreaks(0.5, 1.5)


def pickBronzeBar():
    moveToWithVar(219, 511)
    randomBreaks(0.5, 1.5)


def pickIronBar():
    moveToWithVar(269, 516)
    randomBreaks(0.5, 1.5)


def pickSteelBar():
    moveToWithVar(317, 517)
    randomBreaks(0.5, 1.5)


def pickMithrilBar():
    moveToWithVar(362, 513)
    randomBreaks(0.5, 1.5)

