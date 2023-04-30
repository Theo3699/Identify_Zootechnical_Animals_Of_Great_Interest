import cv2
import numpy as np

# Load the input image in grayscale
img = cv2.imread('images\\testenhancednonostrils.png', cv2.IMREAD_GRAYSCALE)

# Apply Scharr filter in x and y direction
scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)

# Combine the results from both directions to obtain the final edge map
scharr_edges = cv2.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)

# Display the result
cv2.imwrite('cv\\scharr.png', scharr_edges)