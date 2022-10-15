import numpy as np
import cv2, random
from .window import screenshotWin, workAreaImage, getCenterScreen, getCenterMinimap, getWindow
from .support import moveToWithVar, logMsg
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


def findObject(object, vari = 1, cropX = 10, cropY = 40):
    screenshotWin()
    image = cv2.imread(f'{TEMP}screenshot.png')
    contours = findContour(image, object)

    if len(contours) != 0:
        c = max(contours, key=cv2.contourArea)
        x , y = getContourPosition(c)
        moveToWithVar(x + cropX, y + cropY, False, vari)


def getNearest():
    screenshotWin()
    image = cv2.imread(f'{TEMP}screenshot.png')
    contours = findContour(image, object)

    centers = []
    for cont in contours:
        x, y = getContourPosition(cont)
        if x != 0 and y != 0:
            centers.append((x, y))

    if not centers:
        logMsg('Nothing Found', True)
        return

    dims = image.shape
    nearest = getNearestPoint((int(dims[1] / 2), int(dims[0] / 2)), centers)
    return nearest.x + 10, nearest.y + 40


def getNearestPoint(point: tuple, points: list) -> tuple:
    point = (point.x, point.y)
    nodes = np.asarray(points)
    dist2 = np.sum((nodes - point) **2, axis=1)
    p = np.argmin(dist2)
    return points[p][0], points[p][1]

