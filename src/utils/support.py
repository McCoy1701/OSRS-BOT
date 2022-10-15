import pyautogui, random, os
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


def shiftClick(x, y):
    pyautogui.keyDown('shift')
    moveToClick(x, y, (0.02, 0.07), (0.01, 0.05))
    pyautogui.keyUp('shift')


def moveToWithVar(a, b, _shiftClick: bool = False, vari = 5, clicker = 'left'):
    x = random.randrange(a - vari, a + vari)
    y = random.randrange(b - vari, b + vari)
    if not _shiftClick:
        moveToClick(x, y, (0.1, 0.2), (0.01, 0.05), clicker)
    else:
        shiftClick(x, y)


def dropItem():
    pressKey('shift', 0.059, 0.069)


def releaseDropItem():
    pyautogui.keyUp('shift')
    randomBreaks(0.2, 0.3)
    pyautogui.press('shift')
    randomBreaks(0.2, 0.3)


def pointNorth():
    moveToWithVar(617, 89)


def toggleRun():
    moveToWithVar(580, 191)


def clickPrayer():
    moveToWithVar(x, y)


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


def clear():
    os.system('cls')


def logMsg(msg: str, overwrite: bool = False):
    if not overwrite:
        clear()
        print(f'\n{msg}')

    else:
        print(f'\r{msg}', end='')

