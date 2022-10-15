import pyautogui, random, time


def randomBreaks(minSec, maxSec):
    e = random.uniform(minSec, maxSec)
    # print(f'{e}')
    time.sleep(e)


def timer():
    startTime = time.time()
    return startTime


def randomInvo(text, button):
    print(f'{text}')
    pyautogui.press(button)
    randomBreaks(1.5, 15)
    pyautogui.press(button)
    randomBreaks(1.5, 2)
    pyautogui.press('esc')
    return True


def randomPause():
    b = random.uniform(20, 80)
    print(f'Random Pause for {str(b)} secs')
    time.sleep(b)
    return True


options = {
    0: randomInvo,
    1: randomPause}


invoOptions = {
    0: ['Combat Tab', 'f1'],
    1: ['Skills Tab', 'f2'],
    2: ['Equipment Tab', 'f3']}


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


def randomizer(timerBreaks, iBreaks):
    # test = timer()
    # print(f'{iBreaks, timerBreaks} test: {test - timerBreaks} {test - timerBreaks > iBreaks}')
    if _randomBreak(timerBreaks, iBreaks):
        timerBreak = timer()
        iBreak = random.randrange(300, 600)
        return timerBreak, iBreak               # timerBreaks, iBreaks
