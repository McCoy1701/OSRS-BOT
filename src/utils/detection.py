import numpy as np
import cv2, pyautogui, random, win32gui, os, pytesseract
from PIL import Image
from .window import screenshotWin, workAreaImage, inventCrop
from .support import moveToClick
from .settings import *


pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'


def imageToText(preprocess, image, parse_config = '--psm 8') -> str:
    image = cv2.imread(image)
    image = cv2.bitwise_not(image)
    GRAY = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if preprocess == 'thresh':
        GRAY = cv2.threshold(GRAY, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    if preprocess == 'blur':
        GRAY = cv2.medianBlur(GRAY, 3)

    if preprocess == 'adaptive':
        GRAY = cv2.adaptiveThreshold(GRAY, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    filename = '{}.png'.format(os.getpid())
    cv2.imwrite(filename, GRAY)

    with Image.open(filename) as im:
        text = pytesseract.image_to_string(im, config=parse_config)

    os.remove(filename)
    newText = "".join(text.split())
    return newText


def imageRectSingle(image, iHeight, iWidth, threshold, clicker, iSpace = 20, cropX = 0, cropY = 0) -> None:
    workAreaImage()
    loc, w, h, imgBGR = convertToGrayscale(f'{TEMP}workArea.png', f'{IMAGES}{image}', threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(imgBGR, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        x = random.randrange(iWidth, iWidth + iSpace) + cropX
        y = random.randrange(iHeight, iHeight + iSpace) + cropY
        iCoord = pt[0] + iHeight + x
        iCoord = (iCoord, pt[1] + iWidth + y)
        moveToClick(iCoord[0], iCoord[1], (0.2, 0.7), (0.1, 0.3), clicker)

    # cv2.imshow('image', np.hstack([imgBGR, imgGRAY]))
    # cv2.waitKey(0)


def imageRectClicker(image, iHeight, iWidth, threshold, clicker, iSpace = 20, cropX = 0, cropY = 0) -> None:
    screenshotWin()
    loc, w, h, imgBGR = convertToGrayscale(f'{TEMP}screenshot.png', f'{IMAGES}{image}', threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(imgBGR, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        x = random.randrange(iWidth, iWidth + iSpace) + cropX
        y = random.randrange(iHeight, iHeight + iSpace) + cropY
        iCoord = pt[0] + iHeight + x
        iCoord = (iCoord, pt[1] + iWidth + y)
        moveToClick(iCoord[0], iCoord[1], (0.1, 0.3), (0.05, 0.15), clicker)


def imageCount(object, threshold = 0.8, left = 0, top = 0, right = 0, bottom = 0) -> int:
    counter = 0
    screenshotWin(left, top, right, bottom, name='screenshot.png')
    loc, w, h, imgBGR = convertToGrayscale(f'{TEMP}screenshot.png', f'{IMAGES}{object}', threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(imgBGR, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    return counter


def inventCount(object, threshold = 0.8)-> int:
    counter = 0
    inventCrop()
    loc, w, h, imgBGR = convertToGrayscale(f'{TEMP}inventShot.png', f'{IMAGES}{object}', threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(imgBGR, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    return counter


def inventoryEnabled() -> int:
    return imageCount(f'{IMAGES}inventoryEnabled.png', threshold=0.95)


def skillLevelUp() -> int:
    counter = 0
    screenshotWin()
    loc, w, h, imgBGR = convertToGrayscale(f'{TEMP}screenshot.png', f'{IMAGES}congrats.png', threshold=0.8)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(imgBGR, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    return counter


def convertToGrayscale(searchArea, target, threshold):
    imgBGR = cv2.imread(searchArea)
    imgGRAY = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(target, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(imgGRAY, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    return loc, w, h, imgBGR
