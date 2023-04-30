import cv2
import numpy as np

# Load the fingerprint image
img = cv2.imread('images\\test.jpg', 0)

# Apply Otsu's thresholding
_, thresh = cv2.threshold(img, 165, 255, cv2.THRESH_BINARY)
cv2.imshow('otsu', thresh)

# Define the parameters for the Gabor filter
ksize = 5
sigma = 1.0
theta = 0
lambd = 10.0
gamma = 0.5

# Create the Gabor kernel
kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, 0, ktype=cv2.CV_32F)

# Apply the Gabor filter to the image
filtered_img = cv2.filter2D(img, cv2.CV_8UC3, kernel)

# Threshold the filtered image to highlight the ridges
_, thresh = cv2.threshold(filtered_img, 80, 255, cv2.THRESH_BINARY)

# Display the result
cv2.imshow('Original Image', img)
# cv2.imshow('Filtered Image', filtered_img)
# cv2.imshow('Thresholded Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()