"""
Let's take a closer look at color spaces
You may have remembered we talked about images being stored in RGB (Red Green Blue) color Spaces. Let's take a look at that in OpenCV.
First thing to remember about OpenCV's RGB is that it's BGR (I know, this is annoying)
Let's look at the image shape again. The '3L' 
"""

# Import necessary packages
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

# Get the current directory path
dir = os.path.dirname(__file__)

# Load an image
image = cv2.imread(os.path.join(dir, "../../Images/Image.jpg"))

# Check if the image was loaded
if image is None:
    print("Error: Could not read the image.")
    exit()

# Lets check the values of the first pixel
R,G,B = image[0,0]
print(f"{R},{G},{B}")   # Output: 237,236,240
print(image.shape)      # Output: (720, 1280, 3)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_image[0,0])  # Output: 237
print(gray_image.shape) # Output: (720, 1280)

# Did you notice that the first pixel values have 3 dimensions while the second pixel values have 2 dimensions?

# OpenCV's 'split' function splites the image into each color index
B, G, R = cv2.split(image)

print B.shape

row, col = 1, 3
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()
 
axs[0].imshow(cv2.cvtColor(R, cv2.COLOR_BGR2RGB))
axs[0].set_title('Red')

axs[1].imshow(cv2.cvtColor(G, cv2.COLOR_BGR2RGB))
axs[1].set_title('Green')

axs[2].imshow(cv2.cvtColor(B, cv2.COLOR_BGR2RGB))
axs[2].set_title('Blue')

plt.show()