import cv2
import numpy as np

# Load the image
img = cv2.imread('intermediary\\proc2_sobel_contrast_nonoise_contrast_otsu.png')

# Reverse the colors
img_reversed = np.uint8(255 - img)

# Save the result to a file
cv2.imwrite('intermediary\\proc2_sobel_contrast_nonoise_contrast_otsu_reversed.png', img_reversed)