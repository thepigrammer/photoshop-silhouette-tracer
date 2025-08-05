import pyautogui
import random
import time

# Draws 4 ways diagonally from given coordinate to edge of silouette. 
# The original, untraced screenshot should be passed to the "image" parameter.
def checkDiagonals(x, y, image):
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

# Find out what the user wants to do.
while True:
    answer = input('\nTrace over silouette: "trace"\nAdd a blank layer: "layer"\nRename layer: "rename"\nPlace an image: "place"\n\nWhat do you want to do? ')
    if answer == "trace" or answer == "layer" or answer == "rename" or answer == "place":
        break

# Ask the user how many images/tabs are involved.
times = int(input("How many image tabs are there? "))

# If user wants to trace silouette:
if answer == "trace":

    # Record the start time to print total runtime later.
    start = time.time()

    # Click the photoshop elements icon on the taskbar (window must be set up and opened already).
    pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))
    time.sleep(0.5)

    # Go through the image window in the screenshot, drawing diagonally from each black pixel found, for each tab.
    for _ in range(times):
        
        # Store original silouette for drawing diagonals to edge with checkDiagonals().
        originalImage = image = pyautogui.screenshot()

        # Go through image window 4 times, getting more precise with each pass.
        for i in (100, 50, 25, 1):
            
            # Start at top left of image window and trace silouette.
            x = 82
            y = 120
            for y in range(y, 1159, i):
                for x in range(x, 2209, i):

                    # Check current screen for untraced pixels.
                    if image.getpixel((x, y)) == (0, 0, 0):
                        checkDiagonals(x, y, originalImage)
                        image = pyautogui.screenshot()
                x = 82
        
        # Next tab.
        pyautogui.keyDown("ctrl")
        time.sleep(1)
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("ctrl")

# If user wants to add blank layer or rename layer:
elif answer == "layer" or answer == "rename":
    name = input("What do you want to name the layers? ")
    
    # Record the start time to print total runtime later.
    start = time.time()

    # Click the photoshop elements icon on the taskbar (window must be set up and opened already).
    pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))
    time.sleep(0.5)
    
    # Add and/or name the layer for each tab.
    for _ in range(times):

        # Click to add new layer.
        if answer == "layer":
            pyautogui.click(2249, 109)

        # Click to name layer, type the name, then "Enter" to submit it.
        pyautogui.doubleClick(2364, 172)
        pyautogui.write(name + '\n')

        # Needs extra time to catch up for longer names.
        time.sleep(0.05 * len(name))

        # Next tab.
        pyautogui.keyDown("ctrl")
        time.sleep(0.1)
        pyautogui.press("tab")
        time.sleep(0.1)
        pyautogui.keyUp("ctrl")

    # Needs extra time at end to catch up/stop bug.
    time.sleep(3)

# If user wants to place an image as a new layer:
elif answer == "place":
    name = input("What do you want to name the layers? ")
    skips = int(input("How many images should be skipped between each new one? "))

    # Record the start time to print total runtime later.
    start = time.time()

    # Click the photoshop elements icon on the taskbar (window must be set up and opened already).
    pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))
    time.sleep(0.5)

    # Place image and new its layer for each tab.
    for i in range(times):

        # Click "File", then "Place".
        pyautogui.click(64, 22)
        time.sleep(0.1)
        pyautogui.click(148, 336)
        time.sleep(0.5)

        # Click on the first image in the top left of file view.
        pyautogui.click(277, 179)

        # Choose file from first one, dependant on the tab (i).
        for _ in range(i):
            
            # Go to next image, dependant on the skips requested.
            for _ in range(1 + skips):
                pyautogui.press("right")

        # Place image and name its layer.
        pyautogui.press("Enter")
        time.sleep(0.1)
        pyautogui.press("Enter")
        pyautogui.doubleClick(2364, 172)
        pyautogui.write(name + '\n')

        # Needs extra time to catch up for longer names.
        time.sleep(0.05 * len(name))

        # Next tab.
        pyautogui.keyDown("ctrl")
        time.sleep(0.1)
        pyautogui.press("tab")
        time.sleep(0.1)
        pyautogui.keyUp("ctrl")


# Hide photoshop back into taskbar.
time.sleep(0.5)
pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))

# Print runtime in minutes.
print(((time.time() - start) / 60), "minutes")