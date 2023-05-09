import cv2

def enhance_edges(input):
    print('Enhancing edges...')
    # Read the original image
    img = cv2.imread('input\\' + input + '.jpg')

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

    # Sobel Edge Detection
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)  # Sobel Edge Detection on the X axis

    # sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    # sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    #
    # sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

    output = input + '_edges'

    # Display Sobel Edge Detection Images
    cv2.imwrite('intermediary\\' + output + '.jpg', sobelx)
    return output