""" 
HSV is the Hue, Saturation, and Value color model, replaces the RGB (Red, Green, and Blue)
Its very useful in filtering 
"""
# Import necessary packages
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

# Get the current directory path
dir = os.path.dirname(__file__)

# Load an image
image = cv2.imread(os.path.join(dir, "../../Images/flower.jpg"))
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Check if the image was loaded
if image is None:
    print("Error: Could not read the image.")
    exit()

# Display the image
row, col = 2, 2
fig, axs = plt.subplots(row, col, figsize=(12,10))
fig.tight_layout()

# Convert the image to HSV
axs[0][0].imshow(cv2.cvtColor(hsv_image, cv2.COLOR_BGR2RGB))
axs[0][0].set_title('HSV image 0')

axs[0][1].imshow(cv2.cvtColor(hsv_image[:,:,0], cv2.COLOR_BGR2RGB))
axs[0][1].set_title('HSV image 1')

axs[1][0].imshow(cv2.cvtColor(hsv_image[:,:,1], cv2.COLOR_BGR2RGB))
axs[1][0].set_title('HSV image 2')

axs[1][1].imshow(cv2.cvtColor(hsv_image[:,:,2], cv2.COLOR_BGR2RGB))
axs[1][1].set_title('HSV image 3')

plt.show()

# Save the image
# output_path = os.path.join(dir, "./output.jpg")
# cv2.imwrite(output_path, image)

print('Image saved successfully.')