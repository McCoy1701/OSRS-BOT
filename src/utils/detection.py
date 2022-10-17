import numpy as np
import cv2, pyautogui, random, win32gui, os, pytesseract
from PIL import Image
from ..utils.window import screenshotWin, workAreaImage, inventCrop
from ..utils.support import moveToClick
from ..utils.settings import *


pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'


def imageToText(preprocess, image, parse_config = '--psm 7') -> str:
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
    cv2.imwrite(f'{TEMP}{filename}', GRAY)

    with Image.open(f'{TEMP}{filename}') as im:
        text = pytesseract.image_to_string(im, config=parse_config)

    if os.path.exists(fr'{TEMP}{filename}'):
        os.remove(fr'{TEMP}{filename}')
    newText = "".join(text.split())
    return newText


def imageRectSingle(image, func, iHeight, iWidth, threshold, clicker = 'left', iSpace = 5, cropX = 10, cropY = 40) -> None:
    screenshot = func()
    loc, w, h, imgBGR = convertToGrayscale(screenshot, f'{IMAGES}{image}', threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(imgBGR, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        x = random.randrange(iWidth - iSpace, iWidth + iSpace) + cropX
        y = random.randrange(iHeight - iSpace, iHeight + iSpace) + cropY
        iCoord = pt[0] + iHeight + x
        iCoord = (iCoord, pt[1] + iWidth + y)
        moveToClick(iCoord[0], iCoord[1], (0.2, 0.7), (0.1, 0.3), clicker)


def isImageInRect(image, func, threshold = 0.8) -> None:
    screenshot = func()
    loc, _, _, _ = convertToGrayscale(screenshot, f'{IMAGES}{image}', threshold)
    if loc[0] != 0 and loc[1] != 0:
        return True
    else:
        return False


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

