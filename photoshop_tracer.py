import pyautogui
import random
import time

def checkDiagonals(x, y):
    tempX = x
    tempY = y
    while pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX -= 50
        tempY -= 50
    while not pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX += 1
        tempY += 1
    tempX += 3
    tempY += 3
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.moveTo(tempX, tempY)
    tempX -= 2 + random.randint(0, 3)
    tempY -= 2 + random.randint(0, 3)
    pyautogui.moveTo(tempX, tempY)
    tempX += 2 + random.randint(0, 3)
    tempY += 2 + random.randint(0, 3)
    pyautogui.moveTo(tempX, tempY)
    pyautogui.mouseUp()
    tempX = x
    tempY = y
    while pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX += 50
        tempY -= 50
    while not pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX -= 1
        tempY += 1
    tempX -= 3
    tempY += 3
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.moveTo(tempX, tempY)
    tempX += 2 + random.randint(0, 3)
    tempY -= 2 + random.randint(0, 3)
    pyautogui.moveTo(tempX, tempY)
    tempX -= 2 + random.randint(0, 3)
    tempY += 2 + random.randint(0, 3)
    pyautogui.moveTo(tempX, tempY)
    pyautogui.mouseUp()
    tempX = x
    tempY = y
    while pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX -= 50
        tempY += 50
    while not pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX += 1
        tempY -= 1
    tempX += 3
    tempY -= 3
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.moveTo(tempX, tempY)
    tempX -= 2 + random.randint(0, 3)
    tempY += 2 + random.randint(0, 3)
    pyautogui.moveTo(tempX, tempY)
    tempX += 2 + random.randint(0, 3)
    tempY -= 2 + random.randint(0, 3)
    pyautogui.moveTo(tempX, tempY)
    pyautogui.mouseUp()
    tempX = x
    tempY = y
    while pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX += 50
        tempY += 50
    while not pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX -= 1
        tempY -= 1
    tempX -= 3
    tempY -= 3
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.moveTo(tempX, tempY)
    tempX += 2 + random.randint(0, 3)
    tempY += 2 + random.randint(0, 3)
    pyautogui.moveTo(tempX, tempY)
    tempX -= 2 + random.randint(0, 3)
    tempY -= 2 + random.randint(0, 3)
    pyautogui.moveTo(tempX, tempY)
    pyautogui.mouseUp()
    tempX = x
    tempY = y


start = time.time()

pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))

x = 82
y = 120

for y in range(y, 1159, 20):
    for x in range(x, 2209, 100):
        if pyautogui.pixelMatchesColor(x, y, (0, 0, 0), tolerance=10):
            checkDiagonals(x, y)
    x = 82

print(((time.time() - start) / 60), "minutes")