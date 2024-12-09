"""
Grayscaling
Grayscaling is process by which an image is converted from a full color to shades of grey (black & white)

In OpenCV, many functions grayscale images before processing. This is done because it simplifies the image, acting almost as a noise reduction and increasing processing time as there is less information in the image.

Let convert our color image to greyscale
"""

import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

# Import the necessary packages
import cv2
# cv2.__version__ # version number

# Get the current directory path (__file__ means the current directory)
dir = os.path.dirname(__file__)

image = cv2.imread(os.path.join(dir, '../../images/flower.jpg'))

if image is None:
    print('Error: Could not read the image.')
    exit()

# Convert the input color image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the layout of subplots (1 row, 2 columns)
row, col = 1, 2

# Create the figure and subplots with a specific size
# Setting the size of the figure (width=15, height=10 in inches).
fig, axs = plt.subplots(row, col, figsize=(15, 10))

# Automatically adjust spacing between subplots
fig.tight_layout()

# Display the original image in the first subplot
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for Matplotlib
axs[0].set_title('Original')

# Display the grayscale image in the second subplot
axs[1].imshow(gray_image, cmap='gray')
axs[1].set_title('Grayscale')

# Show the figure with the subplots
plt.show()

# Output path
output_path = os.path.join(dir, './Grayscale.jpg')

# Simply use 'imwrite' specificing the file name and the image to be saved
cv2.imwrite(output_path, gray_image)