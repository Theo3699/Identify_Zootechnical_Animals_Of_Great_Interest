import cv2
import numpy as np

image = cv2.imread('grayscale_images\\cow1enhancedsobelxy.png')

kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(image, kernel, iterations = 1)

cv2.imwrite('images\\test.png', erosion)