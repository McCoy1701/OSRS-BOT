import pyautogui, random, time, cv2
import numpy as np

from src.utils.detection import imageToText
from src.utils.screen import workAreaImage, resizeImage
from src.utils.breaks import randomBreaks, randomizer
from src.utils.support import spaces
from src.utils.settings import *

j = 0

monsterArray = [['chicken'], ['cow'], ['guard'], ['monk']]
monsters = ['chicken', 'cow', 'guard', 'monk']

def powerAttack(monster = 'chicken'):
    while True:
        randomizer(timerBreak, iBreak)
        resizeImage()
        status = imageToText('thresh', 'images/textshot.png')

        if status.lower() != monster:
            # print(f'{newText.lower()}')
            randomBreaks(2, 3)
            findAreaAttack(3, 150, 150, 5)
            randomBreaks(4, 5)

        if skillLevelUp() != 0:
            randomBreaks(0.2, 3)
            pyautogui.press('space')
            randomBreaks(0.2, 3)
            pyautogui.press('space')
            a = random.randrange(0, 2)
            spaces(a)
