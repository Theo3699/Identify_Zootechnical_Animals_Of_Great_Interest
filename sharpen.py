import cv2
import numpy as np

# Load the image
img = cv2.imread('images\\testenhancednonostrils.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur with a kernel size of 5x5
img_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Apply Laplacian operator with a kernel size of 3x3
laplacian = cv2.Laplacian(img_blur, cv2.CV_64F, ksize=3)

# Apply zero-crossing to the Laplacian result
edges = cv2.Canny(np.uint8(np.absolute(laplacian)), 50, 150)

# Display result
cv2.imshow('LoG', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()