import cv2
import numpy as np

# Load two images
img1 = cv2.imread('intermediary\\cattle11_edges.png')
img2 = cv2.imread('intermediary\\cattle15_edges.png')

# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Initialize feature detector
orb = cv2.ORB_create()

# Find keypoints and descriptors in both images
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# Initialize matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match keypoints in both images
matches = bf.match(des1, des2)

# Sort matches by distance
matches = sorted(matches, key = lambda x:x.distance)

# Keep only top 10% matches
num_good_matches = int(len(matches) * 0.1)
matches = matches[:num_good_matches]

# Draw matches between images
result = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=2)

# Display result
cv2.imshow('Correlated Images', result)
cv2.waitKey(0)
cv2.destroyAllWindows()