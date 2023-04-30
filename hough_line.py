import cv2
import numpy as np

img = cv2.imread('images\\test.jpg', 0)

kernelx = np.array([[1, 0], [0, -1]])
kernely = np.array([[0, 1], [-1, 0]])

# Apply Roberts edge detection with the diagonal kernels
edgesx = cv2.filter2D(img, -1, kernelx)
edgesy = cv2.filter2D(img, -1, kernely)

# Combine the diagonal edges
edges = cv2.bitwise_or(edgesx, edgesy)

cv2.imshow('Lines Detected', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()