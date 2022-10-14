import pyautogui, random
from .breaks import randomBreaks


def moveToClick(x, y, fst: tuple, sec: tuple, clicker='left') -> None:
    b = random.uniform(fst[0], fst[1])
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(sec[0], sec[1])
    pyautogui.click(duration=b, button=clicker)


def pressKey(key, x, y):
    pyautogui.keyUp(key)
    randomBreaks(x, y)
    pyautogui.keyDown(key)


def dropItem():
    pressKey('shift', 0.059, 0.069)


def releaseDropItem():
    pyautogui.keyUp('shift')
    randomBreaks(0.2, 0.3)
    pyautogui.press('shift')
    randomBreaks(0.2, 0.3)


def pickItem(v, u):
    x = random.randrange(v - 5, v + 5)
    y = random.randrange(u - 5, u + 5)
    moveToClick(x, y, (0.2, 0.6), (0.05, 0.15))
    # print(f'Picked Item: X, Y: {x, y}')


def pointNorth():
    x = random.randrange(617 - 5, 617 + 5)
    y = random.randrange(89 - 5, 89 + 5)
    moveToClick(x, y, (0.2, 0.6), (0.05, 0.15))


def toggleRun():
    x = random.randrange(580 - 5, 580 + 5)
    y = random.randrange(191 - 5, 191 + 5)
    moveToClick(x, y, (0.2, 0.6), (0.05, 0.15))


def clickPrayer():
    moveToClick(x, y, (0.2, 0.6), (0.05, 0.15))


def tiltUp():
    pressKey('up', 0.9, 1)


def tiltDown():
    pressKey('down', 0.9, 1)


def panLeft():
    pressKey('left', 0.9, 1)


def panRight():
    pressKey('right', 0.9, 1)


def spaces(a):
    for x in range(a):
        pressKey('space', 0.05, 0.1)


def shiftClick(x, y):
    pyautogui.keyDown('shift')
    moveToClick(x, y, (0.02, 0.07), (0.01, 0.05))
    randomBreaks(0.1, 0.5)
    pyautogui.keyUp('shift')


def logMsg(msg: str, overwrite: bool = False):
    if not overwrite:
        print(msg)

    else:
        print(f'\r{msg}', end='')

