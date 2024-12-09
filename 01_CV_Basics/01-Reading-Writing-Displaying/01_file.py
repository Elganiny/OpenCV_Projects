"""
    Example: Reading / Writing / Displaying an image 
"""
# Import all the packages that you need
import cv2
import os
from matplotlib import pyplot as plt
import numpy as np

# Print a success message when all the packages are imported
print("Packages imported successfully")

# We do not need to import cv2 again, but it's a good habit
import cv2 

# Get the current directory path (__file__ means the current directory)
dir = os.path.dirname(__file__)

# Load an image using 'imread' command specifying the path to the image
image = cv2.imread(os.path.join( dir, "../../Images/abraham.jpg" ))

# Our file 'input.jpg' is now loaded and stored in python 
# as a varaible we named 'image'

# Check if the image was loaded correctly
if image is None:
    print("Error: Could not read the image.")
    exit()

# To display our image variable, we use 'imshow'
# The first parameter will be title shown on image window
# The second parameter is the image variable

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Abraham Lincoln')

plt.show()

# This command prints the image dimensions
print('Image dimensions = ',image.shape)

# Lets print each dimension
print('Height of the Image =', image.shape[0], ' Pixels')
print('Width of the Image =', image.shape[1], ' Pixels')

# Output path

output_path = os.path.join(dir, "./output.jpg")

# Save the displayed image to a file
cv2.imwrite(output_path, image)

print('Image saved successfully.')


# Wait for a key press before closing the window
cv2.waitKey()