from __future__ import print_function
from __future__ import division
import cv2 as cv
import argparse


def get_principal_components(input):
    print('Extracting principal components...')
    parser = argparse.ArgumentParser(description='Code for Introduction to Principal Component Analysis (PCA) tutorial.\
                                                  This program demonstrates how to use OpenCV PCA to extract the orientation of an object.')
    parser.add_argument('--input', help='Path to input image.', default='pca_test1.jpg')
    args = parser.parse_args()
    src = cv.imread('intermediary\\' + input + '.jpg')
    # Check if image is loaded successfully
    if src is None:
        print('Could not open or find the image: ', args.input)
        exit(0)

    # Convert image to grayscale
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # Convert image to binary
    _, bw = cv.threshold(gray, 50, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    contours, _ = cv.findContours(bw, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    for i, c in enumerate(contours):
        # Calculate the area of each contour
        area = cv.contourArea(c)
        # # Ignore contours that are too small or too large
        # if area < 1e2 or 1e5 < area:
        #     continue
        if area < 1e2:
            continue
        # Draw each contour only for visualisation purposes
        cv.drawContours(src, contours, i, (0, 0, 255), 2)
    output = input + '_pca'
    cv.imwrite('intermediary\\' + output + '.jpg', src)
    return output