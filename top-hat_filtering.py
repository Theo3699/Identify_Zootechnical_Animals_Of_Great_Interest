import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import disk, white_tophat
import cv2

# Load the image
image = plt.imread('images\\testenhancednonostrils.png')

# Convert the image to grayscale
image_gray = np.mean(image, axis=2)

# Define the size of the structuring element for top-hat filtering
radius = 20
selem = disk(radius)

try:
    # Perform white top-hat filtering to enhance bright features (ridges and input)
    ridges = white_tophat(image_gray, selem)

    # Display the original image and the enhanced ridges and input
    fig, axes = plt.subplots(ncols=2, figsize=(8, 4))
    ax = axes.ravel()

    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('Original image')

    ax[1].imshow(ridges, cmap='gray')
    ax[1].set_title('Enhanced ridges and input')

    for a in ax:
        a.axis('off')

    cv2.imwrite('cv\\ridgesenhanced.png', ridges)

except ValueError as e:
    print("Error: ", e)