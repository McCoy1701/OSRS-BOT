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


def getContourPosition(contour):
    moments = cv2.moments(contour)
    centerX = int(moments["m10"] / moments["m00"])
    centerY = int(moments["m01"] / moments["m00"])
    return centerX, centerY


def findObject(item, cropX = 10, cropY = 40):
    screenshotWin()
    image = cv2.imread(f'{TEMP}screenshot.png')
    contours = findContour(image, item)

    if len(contours) != 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)

        x = random.randrange(x + 2, x + max(w - 2, 3)) + cropX
        y = random.randrange(y + 2, y + max(h - 2, 3)) + cropY
        # print(f'Found Item: {item} at X, y:{x, y}')
        moveToClick(x, y, (0.02, 0.04), (0.001, 0.005))


def findObjectPrecise(object, cropX = 10, cropY = 40):
    screenshotWin()
    image = cv2.imread(f'{TEMP}screenshot.png')
    contours = findContour(image, object)

    if len(contours) != 0:
        c = max(contours, key=cv2.contourArea)
        x , y = getContourPosition(c)
        x1 = random.randrange(x - 1, x + 1)
        y1 = random.randrange(y - 1, y + 1)
        moveToClick(x1 + cropX, y1 + cropY, (0.1, 0.2), (0.01, 0.05))
