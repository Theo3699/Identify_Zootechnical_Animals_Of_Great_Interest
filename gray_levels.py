import cv2
import numpy as np

# Load the input image
input_image = cv2.imread("intermediary\\proc2_sobel_contrast.png")

# Convert the input image to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Normalize the grayscale image to have 5 levels of gray
levels = 20
gray_levels = (levels - 1) * np.divide(gray_image, 255/(levels - 1)).astype(np.uint8)

# Scale the gray levels image to the full 8-bit range [0, 255]
gray_levels_scaled = cv2.normalize(gray_levels, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)

# Save the gray levels image
cv2.imwrite("intermediary\\proc2_sobel_contrast_gray_levels4.png", gray_levels)