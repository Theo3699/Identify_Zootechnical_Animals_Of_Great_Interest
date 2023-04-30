import cv2
import numpy as np

def draw_contour(input):
    # Read the input image in grayscale
    img = cv2.imread('images\\' + input + '.png', 0)

    # Define a structuring element for the morphological operation
    kernel = np.ones((5,5), np.uint8)

    # Apply a morphological closing operation to fill gaps in the contours
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # Find the contours of the binary image after the closing operation
    contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on a copy of the original image
    contour_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contour_img, contours, -1, (255, 0, 0), 2)

    output = input + '_contoured'

    # Display the resulting image
    cv2.imwrite('images\\' + output + '.jpg', contour_img)
    return output