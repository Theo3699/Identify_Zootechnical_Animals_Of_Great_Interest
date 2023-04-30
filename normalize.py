import cv2
import os
import numpy as np

def normalize(grayscale_image):
    intensity_levels = 8

    gray_image = cv2.imread(grayscale_image, 0)

    gray_image = gray_image.astype(np.float32)/255

    result = 255*np.floor(gray_image*intensity_levels+0.5)/intensity_levels
    result = result.clip(0,255).astype(np.uint8)

    # (thresh, blackAndWhiteImage) = cv2.threshold(gray_image, 118, 255, cv2.THRESH_BINARY)

    project_root_dir = os.path.dirname(os.path.abspath(__file__))

    cv2.imwrite(project_root_dir + '\\normalized_images\\test3.jpg', result)


if __name__ == '__main__':
    normalize('C:\\Users\\Theo\\PycharmProjects\\pythonProject\\grayscale_images\\animals-12-01453-g002.png')
