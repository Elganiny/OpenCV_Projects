# Import necessary packages
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

# Get the current directory path
dir = os.path.dirname(__file__)

# Load an image
image = cv2.imread(os.path.join(dir, "../../Images/input.jpg"))

# Check if the image was loaded
if image is None:
    print("Error: Could not read the image.")
    exit()
