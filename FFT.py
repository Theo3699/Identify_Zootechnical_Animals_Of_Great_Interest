import cv2
import numpy as np

# Load the input image
img = cv2.imread('output\\cattle_0500_DSCF3908_aligned_cropped_edges_nonoise_blurred_otsu_pca_contoured_thinned.jpg', cv2.IMREAD_GRAYSCALE)

# Compute the 2D Fourier transform of the image
f = np.fft.fft2(img)

# Shift the zero-frequency component to the center of the spectrum
fshift = np.fft.fftshift(f)

# Compute the magnitude spectrum (absolute values) of the Fourier transform
magnitude_spectrum = 20*np.log(np.abs(fshift))

# Display the original image and its Fourier transform
cv2.imshow('Input Image', img)
cv2.imshow('Magnitude Spectrum', magnitude_spectrum.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()