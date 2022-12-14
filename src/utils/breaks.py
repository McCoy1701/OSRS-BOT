import pyautogui, random, time

from ..utils.support import logMsg, randomBreaks


def timer():
    startTime = time.time()
    return startTime


def randomInvo(text, button):
    logMsg(f'{text}', True)
    pyautogui.press(button)
    randomBreaks(1.5, 15)
    pyautogui.press(button)
    randomBreaks(1.5, 2)
    pyautogui.press('esc')
    return True


def randomPause():
    b = random.uniform(20, 80)
    logMsg(f'Random Pause for {str(b)} secs', True)
    time.sleep(b)
    return True


options = {
    0: randomInvo,
    1: randomPause}


invoOptions = {
    0: ['Combat Tab', 'f1'],
    1: ['Skills Tab', 'f2'],
    2: ['Quest Tab', 'f3'],
    3: ['Equipment Tab', 'f4'],
    4: ['Prayer Tab', 'f5'],
    5: ['Magic Tab', 'f6'],
    6: ['Chat Tab', 'f7'],
    7: ['Friends Tab', 'f8'],
    8: ['Account Tab', 'f9'],
    9: ['Settings Tab', 'f10'],
    10: ['Emotes Tab', 'f11'],
    11: ['Music Tab', 'f12']}


def _randomBreak(start, c):
    startTime = timer()
    a = random.randrange(0, 2)
    if startTime - start > c:
        if a == 1:
            return options[a]()
        elif a == 0:
            b = random.randrange(0, 3)
            return options[a](invoOptions[b][0], invoOptions[b][1])
    else:
        return False

