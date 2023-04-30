import cv2
import numpy as np

# Load the input image
img = cv2.imread('images\\testenhancednonostrils.png', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization to normalize the image
img_norm = cv2.equalizeHist(img)

# Define the Gabor filter parameters
ksize = 7   # kernel size
sigma = 2   # standard deviation of the Gaussian envelope
theta = 0   # orientation in degrees
lambd = 5   # wavelength of the sinusoidal factor
gamma = 0.5 # spatial aspect ratio

# Define the block size for block-wise Gabor filter
block_size = 16

# Compute the block-wise orientation map using Sobel filter
dx = cv2.Sobel(img_norm, cv2.CV_32F, 1, 0, ksize=3)
dy = cv2.Sobel(img_norm, cv2.CV_32F, 0, 1, ksize=3)
orient_map = np.arctan2(dy, dx) * 180 / np.pi
orient_map[orient_map < 0] += 180

# Compute the enhanced image by block-wise Gabor filter
img_enhanced = np.zeros_like(img_norm)
for i in range(0, img_norm.shape[0], block_size):
    for j in range(0, img_norm.shape[1], block_size):
        block = img_norm[i:i+block_size, j:j+block_size]
        block_orient = orient_map[i:i+block_size, j:j+block_size]
        gabor_kernel = cv2.getGaborKernel((ksize, ksize), sigma, np.deg2rad(block_orient.mean()), lambd, gamma)
        block_enhanced = cv2.filter2D(block, cv2.CV_8UC1, gabor_kernel)
        img_enhanced[i:i+block_size, j:j+block_size] = block_enhanced

# Binarize the enhanced image using Otsu's thresholding
_, img_binary = cv2.threshold(img_enhanced, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Display the input, normalized, enhanced, and binarized images
cv2.imshow('Normalized', img_norm)
cv2.imshow('Enhanced', img_enhanced)
cv2.imshow('Binarized', img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()