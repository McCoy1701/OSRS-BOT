from src.utils.window import getWindow
import pyautogui, random

# minimapOffset = x, y
# runOffset = x, y


box = getWindow('RuneLite')
# pyautogui.displayMousePosition()
x = random.randrange(455 - 5, 455 + 5)
y = random.randrange(379 - 5, 379 + 5)
print(f'{x}, {y}')
pyautogui.moveTo(x, y, 1)