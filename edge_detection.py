import cv2

def enhance_edges(input):
    # Read the original image
    img = cv2.imread('intermediary\\' + input + '.jpg')

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

    # Sobel Edge Detection
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)  # Sobel Edge Detection on the X axis

    output = input + '_edges'

    # Display Sobel Edge Detection Images
    cv2.imwrite('intermediary\\' + output + '.jpg', sobelx)
    return output