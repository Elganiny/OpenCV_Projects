"""
Example:
Read an image and display it.
"""

import cv2
import os

image = cv2.imread(os.path.join( os.path.dirname(__file__), "../Images/abraham.jpg" ))

if image is None:
    print("Error: Could not read the image.")
    exit()

cv2.imshow("Image", image)

cv2.waitKey()