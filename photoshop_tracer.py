import pyautogui
import random
import time

# Draws 4 ways diagonally from given coordinate to edge of silouette.
def checkDiagonals(x, y):
    tempX = x
    tempY = y
    r, g, b = image.getpixel((tempX, tempY))
    while r < 10 and g < 10 and b < 10:
        tempX -= 2
        tempY -= 2
        r, g, b = image.getpixel((tempX, tempY))
    while not (r < 10 and g < 10 and b < 10):
        tempX += 1
        tempY += 1
        r, g, b = image.getpixel((tempX, tempY))
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
    r, g, b = image.getpixel((tempX, tempY))
    while r < 10 and g < 10 and b < 10:
        tempX += 2
        tempY -= 2
        r, g, b = image.getpixel((tempX, tempY))
    while not (r < 10 and g < 10 and b < 10):
        tempX -= 1
        tempY += 1
        r, g, b = image.getpixel((tempX, tempY))
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
    r, g, b = image.getpixel((tempX, tempY))
    while r < 10 and g < 10 and b < 10:
        tempX -= 2
        tempY += 2
        r, g, b = image.getpixel((tempX, tempY))
    while not (r < 10 and g < 10 and b < 10):
        tempX += 1
        tempY -= 1
        r, g, b = image.getpixel((tempX, tempY))
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
    r, g, b = image.getpixel((tempX, tempY))
    while r < 10 and g < 10 and b < 10:
        tempX += 2
        tempY += 2
        r, g, b = image.getpixel((tempX, tempY))
    while not (r < 10 and g < 10 and b < 10):
        tempX -= 1
        tempY -= 1
        r, g, b = image.getpixel((tempX, tempY))
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

# Ask the user how many images will be traced.
times = int(input("How many image tabs are there? "))

# Record the start time to print total runtime later.
start = time.time()

# Click the photoshop elements icon on the taskbar (window must be set up and opened already).
pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))

# Go through the image window in the screenshot, drawing diagonally from each black pixel found.
for _ in range(times):
    x = 82
    y = 120
    image = pyautogui.screenshot()
    for y in range(y, 1159, 20):
        for x in range(x, 2209, 100):
            if image.getpixel((x, y)) == (0, 0, 0):
                checkDiagonals(x, y)
        x = 82
    pyautogui.keyDown("ctrl")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.keyUp("ctrl")
    


# Hide photoshop back into taskbar.
pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))

# Print runtime in minutes.
print(((time.time() - start) / 60), "minutes")