import pyautogui

def checkDiagonals(x, y):
    fourSpots = []
    tempX = x
    tempY = y
    while pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX -= 50
        tempY -= 50
    while not pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX += 1
        tempY += 1
    fourSpots.append([tempX, tempY])
    tempX = x
    tempY = y
    while pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX += 50
        tempY -= 50
    while not pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX -= 1
        tempY += 1
    fourSpots.append([tempX, tempY])
    tempX = x
    tempY = y
    while pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX -= 50
        tempY += 50
    while not pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX += 1
        tempY -= 1
    fourSpots.append([tempX, tempY])
    tempX = x
    tempY = y
    while pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX += 50
        tempY += 50
    while not pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX -= 1
        tempY -= 1
    fourSpots.append([tempX, tempY])
    tempX = x
    tempY = y
    for spot in fourSpots:
        pyautogui.click(spot[0], spot[1])
        


pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))

x = 82
y = 120

for y in range(y, 1159, 20):
    for x in range(x, 2209, 100):
        if pyautogui.pixelMatchesColor(x, y, (0, 0, 0), tolerance=10):
            checkDiagonals(x, y)
    x = 82