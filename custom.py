import cv2
import numpy as np

# Load the image
img = cv2.imread('images\\testenhancednonostrils.png')

# Define the region of interest
roi = img[150:200, 250:300]

# Calculate the average color of the region of interest
avg_color_per_row = np.average(roi, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
ref_pixel = np.uint8(avg_color)

# Set a color difference threshold
threshold = 20

# Iterate over all the pixels in the region of interest
for i in range(roi.shape[0]):
    for j in range(roi.shape[1]):
        # Calculate the color difference between the pixel and the reference pixel
        color_diff = np.abs(np.int16(roi[i, j]) - np.int16(ref_pixel))

        # If the color difference exceeds the threshold, turn the pixel black
        if np.any(color_diff > threshold):
            roi[i, j] = [0, 0, 0]

# Show the modified image
cv2.imshow('Modified Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()