import cv2

def binarize(input):
    # Read the input image in grayscale
    img = cv2.imread('intermediary\\' + input + '.jpg', 0)

    # Apply Otsu's method to find the optimal threshold value
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Keep only the pixels that have a value of 0 in the binary image
    thresh[thresh != 0] = 255

    output = input + '_otsu'

    # Save the resulting image
    cv2.imwrite('intermediary\\' + output + '.jpg', thresh)
    return output