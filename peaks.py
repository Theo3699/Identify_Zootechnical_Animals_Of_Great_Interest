import cv2
import numpy as np

# load input image and convert to grayscale
img = cv2.imread('intermediary\\cattle_0500_DSCF3908_aligned_edges_nonoise_blurred.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply Gaussian filter to smooth out noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# compute gradient magnitude using Sobel operator
grad_x = cv2.Sobel(blur, cv2.CV_32F, 1, 0)
grad_y = cv2.Sobel(blur, cv2.CV_32F, 0, 1)
grad_mag = cv2.magnitude(grad_x, grad_y)

# threshold gradient magnitude image to extract high gradient regions
threshold = 250
grad_mag_th = np.zeros_like(grad_mag)
grad_mag_th[grad_mag > threshold] = 255

# apply non-maximum suppression to keep only local maxima
nms_size = 5
grad_mag_sup = cv2.dilate(grad_mag_th, np.ones((nms_size, nms_size), np.uint8))
grad_mag_sup[grad_mag_th == 0] = 0

# find peak coordinates
peaks = np.where(grad_mag_sup == 255)
peaks = np.column_stack((peaks[1], peaks[0]))

# (optional) apply minimum distance constraint to remove overlapping peaks
min_dist = 20000
peaks_filtered = cv2.dilate(grad_mag_sup, np.ones((min_dist, min_dist), np.uint8))
peaks_filtered[grad_mag_sup == 0] = 0
peaks_filtered = np.where(peaks_filtered == 255)
peaks_filtered = np.column_stack((peaks_filtered[1], peaks_filtered[0]))

# draw detected peaks on original image
for peak in peaks_filtered:
    cv2.circle(img, tuple(peak), 3, (0, 0, 255), -1)

# display result
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()