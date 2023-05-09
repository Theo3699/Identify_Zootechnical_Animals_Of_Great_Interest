import cv2

def add_blurr(input):
    print('Adding blur...')
    # Load the image
    img = cv2.imread('intermediary\\' + input + '.jpg', 0)

    # Apply the median filter
    blurred_img = cv2.GaussianBlur(img, (5, 5), 2)

    output = input + '_blurred'

    # Display the original and filtered images
    cv2.imwrite('intermediary\\' + output + '.jpg', blurred_img)
    return output