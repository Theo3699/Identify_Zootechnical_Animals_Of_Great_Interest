import cv2

def remove_noise(input):
    print('Removing noise...')
    # Load the image
    img = cv2.imread('intermediary_results\\' + input + '.jpg', 0)

    # Apply the median filter
    img_median = cv2.medianBlur(img, 5)

    output = input + '_nonoise'

    # Display the original and filtered images
    cv2.imwrite('intermediary_results\\' + output + '.jpg', img_median)
    return output