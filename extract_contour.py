import cv2
import numpy as np

def emphasize_contour(input):
    print('Extracting the contour of the relevant components...')
    # Load the image
    img = cv2.imread('intermediary\\' + input + '.jpg')

    black_img = np.zeros_like(img)

    # Convert the image to HSV color space
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define a range of red color in HSV
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    upper_red2 = np.array([180, 50, 50])
    lower_red2 = np.array([170, 255, 255])

    # Create a mask for red pixels in the image
    mask1 = cv2.inRange(hsv_img, lower_red, upper_red)
    mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Turn all red pixels to white using the mask
    black_img[mask == 255] = [255, 255, 255]

    output = input + '_contoured'

    # Display the modified image
    cv2.imwrite('intermediary\\' + output + '.jpg', black_img)
    return output