import pyautogui, random

from ..utils.detection import imageToText, imageRectSingle, inventCount, imageCount, skillLevelUp
from ..utils.window import actionImage, inventCrop
from ..utils.breaks import randomBreaks, randomizer, timer
from ..utils.support import spaces, dropItem, releaseDropItem

j = 0

def dropFish(type):
    global j
    print(f'Dropping...')
    inventCrop()
    dropItem()
    imageRectSingle(f'{type}.png', 5, 5, 0.9, 'left', 10)
    releaseDropItem()
    j += 1
    print(f'Finished Dropping! Dropped {j} times')

def countFish(type):
    return inventCount(type + '.png')

def countSeaPuzzle():
    return imageCount('seaPuzzle.png')


def powerFisher(type, spot):
    while True:
        randomizer(timerBreak, iBreak)
        actionImage()

        if type == 'prawn' or type == 'lobster':
            inv = 23
        else:
            inv = 24

        fish = countFish(type)
        puzzle = countSeaPuzzle()
        inventory = fish + puzzle
        # print(f'Fish: {inventory}')
        randomBreaks(0.2, 0.3)

        if inventory > inv:
            randomBreaks(0.2, 0.7)
            dropFish(type)
            randomBreaks(0.2, 0.7)

        fishing = imageToText('thresh', 'images/textshot.png')
        # print(f'{fishing}')

        if fishing.lower() != 'fishing':
            randomBreaks(0.2, 3)
            pickFishingSpot(spot, 10)
            randomBreaks(0.1, 3)

        if skillLevelUp() !=0:
            randomBreaks(0.2, 2)
            pyautogui.press('space')
            randomBreaks(0.1, 2)
            pyautogui.press('space')
            a = random.randrange(0, 2)
            spaces(a)
