import cv2
import numpy as np

# Load the input image
input_image = cv2.imread('images\\output_image_connected.jpg')

# Define colors
red = (0, 0, 255)
blue = (255, 0, 0)
black = (0, 0, 0)
white = (230, 230, 230)

black_pixels = input_image[np.where((input_image == black).all(axis=2))]
white_pixels = input_image[np.where((input_image == white).all(axis=2))]

# Convert white pixels to blue
input_image[np.where((input_image >= white).all(axis=2))] = blue

cv2.imshow("Output Image", input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert black pixels to red
input_image[np.where((input_image == black).all(axis=2))] = red

cv2.imshow("Output Image", input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert blue pixels to black
input_image[np.where((input_image == blue).all(axis=2))] = black


cv2.imshow("Output Image", input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()