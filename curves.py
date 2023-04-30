import cv2
import numpy as np
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from scipy import ndimage

image = cv2.imread("images\\testenhancednonostrils.png")

img = cv2.medianBlur(image, 13)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                               cv2.THRESH_BINARY, 45, 0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 3))
kernel1 = np.ones((3, 3), np.uint8)
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
dilate = cv2.dilate(thresh, kernel1, iterations=1)
erode = cv2.erode(dilate, kernel, iterations=1)

# Remove small noise by filtering using contour area
cnts = cv2.findContours(erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

for c in cnts:
    if cv2.contourArea(c) < 800:
        if len(c) > 0:
            cv2.drawContours(thresh, [c], 0, (0, 0, 0), -1)

# Compute Euclidean distance from every binary pixel
# to the nearest zero pixel then find peaks
distance_map = ndimage.distance_transform_edt(erode)
local_max = peak_local_max(distance_map, min_distance=10, threshold_abs=thresh)

# Create an empty binary mask with the same shape as the input image
mask = np.zeros_like(image[:,:,0])

# Set the coordinates of the local maxima to 1 in the mask
mask[local_max[:,0], local_max[:,1]] = 1

# Perform connected component analysis then apply Watershed
markers = ndimage.label(mask, structure=np.ones((3, 3)))[0]
labels = watershed(-distance_map, markers, mask=erode)

# Iterate through unique labels
for label in np.unique(labels):
    if label == 0:
        continue

    # Create a mask
    mask = np.zeros(thresh.shape, dtype="uint8")
    mask[labels == label] = 255

    # Find contours and determine contour area
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    c = max(cnts, key=cv2.contourArea)

    cv2.drawContours(image, [c], -1, (36, 255, 12), -1)

cv2.imwrite('Results/drawedImage.png', image)

thresh = 155
im_bw = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite("images/binary.png", im_bw)