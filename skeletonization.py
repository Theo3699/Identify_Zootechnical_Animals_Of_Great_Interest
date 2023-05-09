import cv2

def thin(input):
    print('Thinning...')
    # Load the binary image
    img = cv2.imread('intermediary\\' + input + '.jpg', cv2.IMREAD_GRAYSCALE)

    # Apply binary thresholding to make sure the image is binary
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Perform the thinning operation using the Zhang-Suen algorithm
    thinned = cv2.ximgproc.thinning(img, cv2.ximgproc.THINNING_ZHANGSUEN)

    output = input + '_thinned'

    # Display the thinned image
    cv2.imwrite('output\\' + output + '.jpg', thinned)
    return output