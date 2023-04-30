import cv2
import numpy as np

# Load input image in grayscale
img = cv2.imread('cv\\testnonostrils_sobelx1.png', 0)

# Set the block size for adaptive thresholding
block_size = 41

# Compute local adaptive threshold for each pixel
adaptive_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, 6)

