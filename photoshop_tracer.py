import pyautogui

def checkDiagonals(x, y):
    fourSpots = []
    tempX = x
    tempY = y
    while pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX -= 5
        tempY -= 5
        pyautogui.moveTo(tempX, tempY)
    fourSpots.append([tempX, tempY])
    tempX = x
    tempY = y
    while pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX += 5
        tempY -= 5
        pyautogui.moveTo(tempX, tempY)
    fourSpots.append([tempX, tempY])
    tempX = x
    tempY = y
    while pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX -= 5
        tempY += 5
        pyautogui.moveTo(tempX, tempY)
    fourSpots.append([tempX, tempY])
    tempX = x
    tempY = y
    while pyautogui.pixelMatchesColor(tempX, tempY, (0, 0, 0), tolerance=10):
        tempX += 5
        tempY += 5
        pyautogui.moveTo(tempX, tempY)
    fourSpots.append([tempX, tempY])
    tempX = x
    tempY = y
    for spot in fourSpots:
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        pyautogui.moveTo(spot[0], spot[1], 0.5)
        pyautogui.mouseUp()


pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))

x = 82
y = 120

for y in range(y, 1159, 10):
    for x in range(x, 2209, 100):
        pyautogui.moveTo(x, y)
        if pyautogui.pixelMatchesColor(x, y, (0, 0, 0), tolerance=10):
            checkDiagonals(x, y)
    x = 82