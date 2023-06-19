import cv2

def remove_noise():
    print('Removing noise...')
    # Load the image
    img = cv2.imread('C:\\Users\\Theo\\PycharmProjects\\pythonProject\\demo\\api\\intermediary\\input_aligned_edges.jpg', 0)

    # Apply the median filter
    img_median = cv2.medianBlur(img, 5)

    output = 'C:\\Users\\Theo\\PycharmProjects\\pythonProject\\demo\\api\\intermediary\\input_aligned_edges_nonoise.jpg'

    # Display the original and filtered images
    cv2.imwrite(output, img_median)