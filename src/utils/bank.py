import cv2, pyautogui, random


def exitBank():
    x = random.randrange(523, 540)
    y = random.randrange(40, 55)
    b = random.uniform(0.15, 0.6)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.19)
    pyautogui.click(duration=b)
    randomBreaks(0.3, 0.7)


def depositSecondItem():
    x = random.randrange(690, 715)
    y = random.randrange(495, 515)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration = b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration = b)
    randomBreaks(0.3, 0.7)


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
