import cv2

def add_blurr():
    print('Adding blur...')
    # Load the image
    img = cv2.imread('C:\\Users\\Theo\\PycharmProjects\\pythonProject\\demo\\api\\intermediary\\input_aligned_edges_nonoise.jpg', 0)

    # Apply the median filter
    blurred_img = cv2.GaussianBlur(img, (5, 5), 2)

    output = 'C:\\Users\\Theo\\PycharmProjects\\pythonProject\\demo\\api\\intermediary\\input_aligned_edges_nonoise_blurred.jpg'

    # # Display the original and filtered images
    cv2.imwrite(output, blurred_img)