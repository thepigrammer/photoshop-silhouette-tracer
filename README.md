### DESCRIPTION
The program uses the brush tool to trace over black pixels detected in an image window in Adobe Photoshop Elements. The edges of the result are made slightly rough (using randomness) to mimic manual tracing. Multiple image tabs can be traced with one run of the program. The program also includes some other features to assist with modifying multiple tabs. Total runtime after receiving user input is printed upon completion.

---

### SETUP REQUIREMENTS
The program was made only to be used with the following:
- Windows 11

- 2560 x 1440 screen resolution
- PyAutoGUI and Pillow modules
- Adobe Photoshop Elements 2024
- Program must have access to "photoshop_icon.png" to get to Photoshop while running. It should be a cropped screenshot of the icon for Photoshop on your Windows taskbar. Photoshop must be open and prepared to draw before running the program.

---

### FEATURES
- "trace" is the main feature. It will look through the image window in Photoshop and trace over pixels that are in the range to be considered a black pixel. The process involves four passes to search for black pixels, getting more precise each time, intended to give a style to the drawn result. The program will save the tab after each pass. Note that the brush tool must be selected before running so that the program can immediately begin drawing when it opens Photoshop.

- "layer" adds a blank layer with a given name to each tab. The layer must be at the top of the list of layers, so the current highest one must be selected before running.
- "rename" renames the top layer in each tab to a given name.
- "place" places an image as a named layer in each tab. This is intended for animation involving multiple frames. The folder containing the frames must be the one open in the file view whenever it is opened in Photoshop. The program will go through each Photoshop tab and add one of the frames depending on which tab is currently being affected. It will move to the next frame for each Photoshop tab, or skip some in between each tab if the user specified a nonzero number when prompted. The selected layer before running must be the highest one in the list of layers.
- "save" will save each Photshop tab, including if it is the first save since opening Photoshop in which the file view will ask if the current version of the file should be overwritten.
- "hide" will click the hide (or unhide) button on a selected layer from the layers list on each tab. The top layer in the layers list is "1", the next one down is "2", etc. This feature assumes that the top of the list is shown, not scrolled down, so that the layer selection is consistent.
- "zoom" will go through each Photoshop tab and zoom in to the part of the image that would be traced if "trace" were used. This is intended to be used before using "trace". The zoom tool in Photoshop must be selected before running.
