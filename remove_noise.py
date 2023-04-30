import cv2

def remove_noise(input):
    # Load the image
    img = cv2.imread('intermediary\\' + input + '.jpg', 0)

    # Apply the median filter
    img_median = cv2.medianBlur(img, 5)

    output = input + '_nonoise'

    # Display the original and filtered images
    cv2.imwrite('intermediary\\' + output + '.jpg', img_median)
    return output