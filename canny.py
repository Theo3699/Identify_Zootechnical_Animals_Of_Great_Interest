import matplotlib.pyplot as plt
import numpy as np
from skimage import feature, morphology

# Load the image
image = plt.imread('images\\test.jpg')

# Convert the image to grayscale
image_gray = np.mean(image, axis=2)

# Apply Canny edge detection to obtain the edges of the image
edges = feature.canny(image_gray, sigma=1)

# Perform morphological skeletonization to obtain the lines
lines = morphology.skeletonize(edges)

# Display the original image and the extracted lines
fig, axes = plt.subplots(ncols=2, figsize=(8, 4))
ax = axes.ravel()

ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original image')

ax[1].imshow(lines, cmap='gray')
ax[1].set_title('Extracted lines')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()