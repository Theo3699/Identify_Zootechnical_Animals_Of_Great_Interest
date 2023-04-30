import cv2
import numpy as np

# Load the input image
img = cv2.imread('cv\\test_sobelx1.png')

# Define a scalar value to make the image darker
scalar = 0.5

# Create a new matrix of ones with the same size as the input image
# and multiply it with the scalar value to create a matrix of the same size
# with scalar values
dark_matrix = np.ones(img.shape, dtype='uint8') * scalar

# Multiply the input image with the dark matrix to make it darker
img_dark = cv2.multiply(img, dark_matrix)

# Display the original and darker images
cv2.imwrite('cv\\sobelx1darken.png', img_dark)
