import numpy as np
import cv2, random
from .window import screenshotWin, workAreaImage, getCenterScreen, getCenterMinimap, getWindow
from .support import moveToClick
from .settings import *


def findContour(image, color: int):
    objects = [RED, GREEN, YELLOW, BLUE, PURPLE, PINK, PICKUP_HIGHLIGHT, ATTACK_BLUE]

    lower = objects[color][0]
    upper = objects[color][1]

    lower = np.array(lower, dtype = 'uint8')
    upper = np.array(upper, dtype = 'uint8')
    mask = cv2.inRange(image, lower, upper)
    # output = cv2.bitwise_and(image, image, mask = mask)
    _, thresh = cv2.threshold(mask, 40, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.imshow('shit', output)
    # cv2.waitKey(0)
    return contours


def findObject(item, cropX = 10, cropY = 40):
    screenshotWin()
    image = cv2.imread(f'{TEMP}screenshot.png')
    contours = findContour(image, item)

    if len(contours) != 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)

        x = random.randrange(x + 5, x + max(w - 5, 6)) + cropX
        y = random.randrange(y + 5, y + max(h - 5, 6)) + cropY
        # print(f'Found Item: {item} at X, y:{x, y}')
        moveToClick(x, y, (0.02, 0.04), (0.001, 0.005))


def findClosestObject(item) -> list[int]:
    images = screenshotWin()
    contours = findContour(images, item)
    winSize = getWindow('RuneLite')
    centerScreen = getCenterScreen(winSize)
    minimap = getCenterMinimap(winSize)

    if contours == ():
        return []

    distance = []

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        distance.append(np.sqrt((x - centerScreen[0])**2 + (y + centerScreen[1])**2))
    minVal = min(distance)
    indexMin = distance.index(minVal)
    x, y, w, h = cv2.boundingRect(contours[indexMin])
    centerX = round(x + w / 2)
    centerY = round(y + h / 2)
    distance = np.sqrt((x - minimap[0])**2 + (y - minimap[1])**2)
    if distance < 100:
        return []
    return [centerX, centerY]


def findAreaAttack(object, cropX = 10, cropY = 40, deep = 1):
    workAreaImage()
    images = cv2.imread(f'{TEMP}workArea.png')
    contours = findContour(images, object)

    if len(contours) != 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        halfW = max(round(w / 2), 1)
        halfH = max(round(h / 2), 1)
        x = random.randrange(x + halfW - deep, x + max(halfW + deep, 1)) + cropX
        y = random.randrange(y + halfH - deep, y + max(halfH + deep, 1)) + cropY
        moveToClick(x, y, (0.01, 0.05), (0.01, 0.05))
        # print(f'Found {object} at {x, y}')


def clickCloset(color: int) -> None:
    x, y = findClosetObject(color)
    moveToClick(x, y, (0.2, 0.7), (0.1, 0.3))

