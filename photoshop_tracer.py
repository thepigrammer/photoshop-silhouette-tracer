import pyautogui

def checkRow(x, y):
    if pyautogui.pixelMatchesColor(x+1, y, (0, 0, 0), tolerance=10):
        pyautogui.mouseDown()
        x += 1
        pyautogui.click(x, y)
        checkRow(x, y)
    

pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))

x = 82
y = 120

for y in range(y, 1159, 3):
    for x in range(x, 2209, 100):
        pyautogui.moveTo(x,y)
        if pyautogui.pixelMatchesColor(x, y, (0, 0, 0), tolerance=10):
            pyautogui.click()
            checkRow(x, y)
    x = 82