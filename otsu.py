import cv2

def binarize(input):
    print('Binarizing image...')
    # Read the input image in grayscale
    img = cv2.imread('intermediary_results\\' + input + '.jpg', 0)

    # Apply Otsu's method to find the optimal threshold value
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Keep only the pixels that have a value of 0 in the binary image
    thresh[thresh != 0] = 255

    output = input + '_otsu'

    # Save the resulting image
    cv2.imwrite('output_results\\' + output + '.jpg', thresh)
    return output