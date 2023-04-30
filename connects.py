
import numpy as np
import cv2

# Read the image of the cow's muzzle print
img_gray = cv2.imread('intermediary\\proc2_sobel.png', cv2.IMREAD_GRAYSCALE)

# Perform connected component labeling to extract the individual ridge patterns
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(img_gray, connectivity=8, ltype=cv2.CV_32S)
colors = [(214, 170, 50), (98, 141, 195), (168, 232, 86), (166, 226, 231), (234, 157, 87), (198, 57, 227), (208, 90, 246), (30, 215, 171)]

# Highlight the ridge patterns with different colors
img_out = np.zeros((img_gray.shape[0], img_gray.shape[1], 3), dtype=np.uint8)
for i in range(1, num_labels):
    mask = labels == i
    color = colors[i % len(colors)]
    img_out[mask] = color

# Display the results
cv2.imwrite('intermediary\\proc2_connected.png', img_out)