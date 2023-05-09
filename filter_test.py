import cv2
import numpy as np

# Load the image
img = cv2.imread('intermediary_results\\cattle_0600_DSCF3917_aligned.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define the filters
f1 = np.array([[0, -1, 0],
               [0, 0, 0],
               [0, 1, 0]])

f2 = np.array([[0, 0, 0],
               [1, 0, -1],
               [0, 0, 0]])

# Apply the filters
filtered1 = cv2.filter2D(gray, -1, f1)
filtered2 = cv2.filter2D(gray, -1, f2)

# Merge the filtered images using element-wise addition
merged = cv2.add(filtered1, filtered2)

# Display the filtered images
cv2.imwrite('Filter_merged2.jpg', merged)