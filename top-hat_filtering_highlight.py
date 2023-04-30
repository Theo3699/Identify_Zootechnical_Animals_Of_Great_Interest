import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import disk, white_tophat, black_tophat, skeletonize

# Load the image
image = plt.imread('images\\testenhancednonostrils.png')

# Convert the image to grayscale
image_gray = np.mean(image, axis=2)

# Define the size of the structuring element for top-hat and skeletonization filtering
radius = 50
selem = disk(radius)

try:
    # Perform white top-hat filtering to enhance bright features (ridges and input)
    ridges = white_tophat(image_gray, selem)

    # Perform black top-hat filtering to enhance dark features (valleys)
    valleys = black_tophat(image_gray, selem)

    # Combine the enhanced ridges and valleys
    ridges = ridges - valleys

    # Binarize the image to highlight the ridges
    threshold = 0.1
    ridges[ridges < threshold * np.max(ridges)] = 0
    ridges[ridges > 0] = 1

    # Skeletonize the binarized image to obtain thin ridges
    ridges = skeletonize(ridges)

    # Display the original image and the enhanced ridges
    fig, axes = plt.subplots(ncols=2, figsize=(8, 4))
    ax = axes.ravel()

    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('Original image')

    ax[1].imshow(ridges, cmap='gray')
    ax[1].set_title('Enhanced ridges')

    for a in ax:
        a.axis('off')

    plt.tight_layout()
    plt.show()

except ValueError as e:
    print("Error: ", e)