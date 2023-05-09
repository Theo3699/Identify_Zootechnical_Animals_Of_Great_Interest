import cv2
import numpy as np

def getPixelFromLeft(img):
    rows, cols, _ = img.shape
    farthest = (0, 0)
    for i in range(rows):
        for j in range(int(cols/2)):
            (b, g, r) = img[i, j]
            if b <= 255 and b >= 250 and g == 0 and r == 0 and j > farthest[1]:
                farthest = (i, j)
    return farthest


def getPixelFromRight(img):
    rows, cols, _ = img.shape
    farthest = (0, 99999999)
    for i in range(rows):
        for j in range(int(cols/2), cols):
            (b, g, r) = img[i, j]
            if b <= 255 and b >= 250 and g == 0 and r == 0 and j < farthest[1]:
                farthest = (i, j)
    return farthest

def crop(input):
    print('Cropping...')
    # Load the image
    img = cv2.imread('intermediary\\' + input + '.jpg')

    # Get the height of the image
    height = img.shape[0]

    # Calculate the pixel values to crop from the top and bottom
    top_crop = int(0.25 * height)
    bottom_crop = int(0.40 * height)

    # Crop the image
    img_cropped = img[top_crop:height - bottom_crop, :]

    # Convert to grayscale
    gray = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to remove noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Compute Otsu's threshold
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Invert the thresholded image
    thresh = cv2.bitwise_not(thresh)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original image
    for contour in contours:
        cv2.drawContours(img, [contour], -1, (255, 0, 0), 2)

    left_pixel = getPixelFromLeft(img)[1]
    right_pixel = getPixelFromRight(img)[1]

    relevant = right_pixel-left_pixel

    x, y, _ = img.shape

    crop_image = img[0:y, left_pixel:left_pixel+relevant]

    output = input + '_cropped'
    cv2.imwrite('intermediary\\' + output + '.jpg', crop_image)
    return output