import pyautogui
import random
import time

def main():

    # Find out what the user wants to do.
    while True:
        print('\nTrace over silhouette: "trace"')
        print('Add a blank layer: "layer"')
        print('Rename layer: "rename"')
        print('Place an image: "place"')
        print('Save after opening photoshop: "save"')
        print('Hide or unhide a layer: "hide"')
        print('Zoom in on silhouette: "zoom"')
        answer = input('\nWhat do you want to do? ')
        if (answer == "trace" or answer == "layer" or answer == "rename" or 
            answer == "place" or answer == "save" or answer == "hide" or
            answer == "zoom"):
            break

    # Ask the user how many images/tabs are involved.
    times = int(input("How many image tabs are there? "))

    # If user wants to trace silhouette:
    if answer == "trace":

        # Record the start time to print total runtime later.
        start = time.time()

        # Click the photoshop elements icon on the taskbar (window must be set up and opened already).
        pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))
        time.sleep(0.5)

        # Go through the image window in the screenshot, drawing diagonally from each black pixel found, for each tab.
        for _ in range(times):
            
            # Store original silhouette for drawing diagonals to edge with drawDiagonals().
            originalImage = image = pyautogui.screenshot()

            # Go through image window 4 times, getting more precise with each pass.
            for i in (100, 50, 25, 1):
                
                # Start at top left of image window and trace silhouette.
                for y in range(120, 1159, i):
                    for x in range(82, 2209, i):

                        # Check current screen for untraced pixels and trace them.
                        r, g, b = image.getpixel((x, y))
                        if r < 50 and g < 50 and b < 50:
                            drawDiagonals(x, y, originalImage)
                            image = pyautogui.screenshot()
                
                # Save after each pass in case photoshop crashes.
                save()
                 
            # Next tab.
            time.sleep(3)
            pyautogui.moveTo(82, 120)
            pyautogui.keyDown("ctrl")
            time.sleep(1)
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("ctrl")
            time.sleep(1)

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
            time.sleep(1)

            # Click on the first image in the top left of file view.
            pyautogui.click(277, 179)

            # Choose file from first one, dependant on the tab (i).
            for _ in range(i):
                
                # Go to next image, dependant on the skips requested.
                for _ in range(1 + skips):
                    pyautogui.press("right")
            
            time.sleep(0.3)
            
            # Place image and name its layer.
            pyautogui.press("Enter")
            time.sleep(0.3)
            pyautogui.press("Enter")
            time.sleep(0.1)
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

    # If user wants to save opened photoshop files:
    elif answer == "save":

        # Record the start time to print total runtime later.
        start = time.time()

        # Click the photoshop elements icon on the taskbar (window must be set up and opened already).
        pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))
        time.sleep(0.5)
        
        for _ in range(times):
                pyautogui.keyDown("ctrl")
                time.sleep(0.1)
                pyautogui.press("s")
                time.sleep(0.1)
                pyautogui.keyUp("ctrl")
                time.sleep(0.1)
                pyautogui.press("Enter")
                time.sleep(0.1)
                pyautogui.press("y")
                time.sleep(0.1)

                pyautogui.keyDown("ctrl")
                time.sleep(0.1)
                pyautogui.press("tab")
                time.sleep(0.1)
                pyautogui.keyUp("ctrl")

    # If user wants to hide or unhide a layer:
    elif answer == "hide":
        layer = int(input('Top layer is "1". Which layer do you want to hide/unhide? '))

        # Record the start time to print total runtime later.
        start = time.time()

        # Click the photoshop elements icon on the taskbar (window must be set up and opened already).
        pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))
        time.sleep(0.5)

        for _ in range(times):
            pyautogui.click(2245, 170 + (39 * (layer - 1)))
            
            pyautogui.keyDown("ctrl")
            time.sleep(0.1)
            pyautogui.press("tab")
            time.sleep(0.1)
            pyautogui.keyUp("ctrl")
            time.sleep(0.1)

    # If user wants to zoom in on silhouette:
    elif answer == "zoom":

        # Record the start time to print total runtime later.
        start = time.time()

        # Click the photoshop elements icon on the taskbar (window must be set up and opened already).
        pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))
        time.sleep(0.5)

        for _ in range(times):
            image = pyautogui.screenshot()

            # Find highest y value.
            top = 0
            for y in range(120, 1159, 1):
                for x in range(82, 2209, 1):
                    r, g, b = image.getpixel((x, y))
                    if r < 50 and g < 50 and b < 50:
                        top = y - 5
                        break
                if top > 0:
                    break
            
            # Find lowest y value:
            bottom = 0
            for y in range(1159, 120, -1):
                for x in range(82, 2209, 1):
                    r, g, b = image.getpixel((x, y))
                    if r < 50 and g < 50 and b < 50:
                        bottom = y + 5
                        break
                if bottom > 0:
                    break

            # Find leftmost x value:
            left = 0
            for x in range(82, 2209, 1):
                for y in range(120, 1159, 1):
                    r, g, b = image.getpixel((x, y))
                    if r < 50 and g < 50 and b < 50:
                        left = x - 5
                        break
                if left > 0:
                    break

            # Find rightmost x value:
            right = 0
            for x in range(2209, 82, -1):
                for y in range(120, 1159, 1):
                    r, g, b = image.getpixel((x, y))
                    if r < 50 and g < 50 and b < 50:
                        right = x + 5
                        break
                if right > 0:
                    break
            
            # Zoom in if silhouette found.
            if right > 0:
                pyautogui.mouseDown(x=left, y=top)
                pyautogui.moveTo(right, bottom)
                pyautogui.mouseUp()

            # Change tabs.
            pyautogui.keyDown("ctrl")
            time.sleep(0.1)
            pyautogui.press("tab")
            time.sleep(0.1)
            pyautogui.keyUp("ctrl")
            time.sleep(0.1)

    # Hide photoshop back into taskbar.
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen("photoshop_icon.png"))

    # Print runtime in minutes.
    print(((time.time() - start) / 60), "minutes")


def save():
    # Save (potentially in file view if first time saving since opening in photoshop).
    time.sleep(1)
    pyautogui.keyDown("ctrl")
    time.sleep(0.1)
    pyautogui.press("s")
    time.sleep(0.1)
    pyautogui.keyUp("ctrl")
    time.sleep(2)
    pyautogui.press("Enter")
    time.sleep(1)
    pyautogui.press("y")
    time.sleep(1)

    # Make sure tool is brush.
    pyautogui.press("y")
    time.sleep(1)
    pyautogui.press("b")
    time.sleep(1)


# Draws 4 ways diagonally from given coordinate to edge of silhouette. 
# The original, untraced screenshot should be passed to the "image" parameter.
def drawDiagonals(x, y, image):
    tempX = x
    tempY = y
    r, g, b = image.getpixel((tempX, tempY))
    while r < 50 and g < 50 and b < 50:
        tempX -= 2
        tempY -= 2
        r, g, b = image.getpixel((tempX, tempY))
    while not (r < 50 and g < 50 and b < 50):
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
    while r < 50 and g < 50 and b < 50:
        tempX += 2
        tempY -= 2
        r, g, b = image.getpixel((tempX, tempY))
    while not (r < 50 and g < 50 and b < 50):
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
    while r < 50 and g < 50 and b < 50:
        tempX -= 2
        tempY += 2
        r, g, b = image.getpixel((tempX, tempY))
    while not (r < 50 and g < 50 and b < 50):
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
    while r < 50 and g < 50 and b < 50:
        tempX += 2
        tempY += 2
        r, g, b = image.getpixel((tempX, tempY))
    while not (r < 50 and g < 50 and b < 50):
        tempX -= 1
        tempY -= 1
        r, g, b = image.getpixel((tempX, tempY))
    tempX -= 3
    tempY -= 3
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.moveTo(tempX, tempY)
    tempX += 2 + random.randint(0, 5)
    tempY += 2 + random.randint(0, 5)
    pyautogui.moveTo(tempX, tempY)
    tempX -= 2 + random.randint(0, 5)
    tempY -= 2 + random.randint(0, 5)
    pyautogui.moveTo(tempX, tempY)
    pyautogui.mouseUp()
    tempX = x
    tempY = y


main()