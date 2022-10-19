import pyautogui, random, time, cv2
import numpy as np

from ..utils.detection import imageToText, imageRectSingle, inventCount, imageCount, skillLevelUp
from ..utils.colorDetection import findObject
from ..utils.window import workAreaImage, actionImage, inventCrop
from ..utils.breaks import randomBreaks, randomizer
from ..utils.support import spaces, dropItem, releaseDropItem

j = 0

def dropOre(type):
    global j
    print(f'Dropping...')
    inventCrop()
    dropItem()
    imageRectSingle(f'{type}Ore.png', 5, 5, 0.9, 'left')
    releaseDropItem()
    j += 1
    print(f'Finished Dropping! Dropped {j} times')

def powerMiner(ore, manual, num):
    powerList = ['tin', 'copper', 'coal', 'iron', 'clay']
    oreIndex = powerList.index(ore)
    # print(f'{oreIndex}')

    while True:
        randomizer(timerBreak, iBreak)

        invoCount = int(inventCount(f'{oreIndex}Ore.png'))
        gemCount = int(inventCount('gem.png'))
        geoCount = int(inventCount('geo.png'))
        inventory = invoCount + gemCount + geoCount
        # print(f'Ores: {invoCount} | Gems: {gemCount} | Clues: {geoCount}')

        if inventory >= 27:
            dropOre(powerList[ore])
            randomBreaks(0.1, 0.2)

        actionImage()
        minedText = imageToText('thresh', 'images/textShot.png')

        if minedText.lower() != 'mining':
            # print(f'{newText}')
            randomBreaks(.5, 2)
            if manual:
                findObject(num, 150, 150)
        if skillLevelUp() != 0:
            randomBreaks(0.2, 3)
            pyautogui.press('space')
            randomBreaks(0.2, 3)
            pyautogui.press('space')
            a = random.randrange(0, 2)
            spaces(a)
