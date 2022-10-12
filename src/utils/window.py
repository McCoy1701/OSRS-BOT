import win32gui
from .settings import *
from PIL import Image, ImageGrab

wnd = 0

def setWindow(name):
    global wnd
    wnd = win32gui.FindWindow(None, name)
    win32gui.MoveWindow(wnd, 10, 40, 809, 534, True)
    win32gui.SetActiveWindow(wnd)
    win32gui.SetForegroundWindow(wnd)


def getWindow(name):
    global wnd
    wnd = win32gui.FindWindow(None, name)
    rect = win32gui.GetWindowRect(wnd)
    x = rect[0]
    y = rect[1] + CLIENT_BORDER[0]
    w = rect[2] - x - CLIENT_BORDER[1]
    h = rect[3] - y - CLIENT_BORDER[0]
    return [x, y, w, h]


def getCenterMinimap(windowSize: list[int]) -> list[float]:
    mapCenterX = windowSize[0] + windowSize[2] - OFFSET_MINIMAP[0]
    mapCenterY = windowSize[1] + windowSize[3] - OFFSET_MINIMAP[1]
    return [mapCenterX, mapCenterY]


def getCenterScreen(windowSize: list[int]) -> list[int]:
    centerX = round(windowSize[0] + windowSize[2] / 2)
    centerY = round(windowSize[1] + windowSize[3] / 2)
    return [centerX, centerY]


def getRunButton(windowSize: list[int]) -> list[int]:
    runX = windowSize[0] + windowSize[2] - OFFSET_RUN[0]
    runY = windowSize[1] + OFFSET_RUN[1]
    return [runX, runY]


def getLogoutButton(windowSize: list[int]) -> list[int]:
    logoutX = windowSize[0] + windowSize[2] - OFFSET_LOGOUT[0]
    logoutY = windowSize[1] + OFFSET_LOGOUT[1]
    return [logoutX, logoutY]


def inventCrop():
    return screenshotWin(562, 270, 755, 535, 'inventShot.png')


def minimapImage():
    return screenshotWin(620, 70, 780, 230, 'minimap.png')


def runImage():
    run = screenshotWin(580, 192, 610, 212, 'runAmount.png')
    return scaleImage(run)


def prayerImage():
    prayer = screenshotWin(570, 160, 600, 180, 'prayerAmount.png')
    return scaleImage(prayer)


def healthImage():
    health = screenshotWin(570, 125, 600, 145, 'healthAmount.png')
    return scaleImage(health)


def workAreaImage():
    return screenshotWin(15, 80, 540, 400, 'workArea.png')


def actionImage():
    action = screenshotWin(35, 90, 132, 110, 'action.png')
    return scaleImage(action)


def scaleImage(img):
    im = Image.open(img)
    width, height = im.size
    newSize = (width * 6, height * 6)
    iml = im.resize(newSize)
    text = img.rsplit('.', 1)
    iml.save(f'{text[0]}Scaled.png')
    return iml


def __save(image, name):
    image.save(rf'{TEMP}{name}')
    return f'{TEMP}{name}'


def screenshotWin(left=10, top=40, right=820, bottom=575, name='screenshot.png'):
    if left != 0 and top != 0 and right != 0 and bottom != 0:
        screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    else:
        screenshot = ImageGrab.grab()
    return __save(screenshot, name)
