import cv2
import numpy as np

# Load the image
img = cv2.imread('input\\cattle_0600_DSCF3923.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection with different threshold values
edges = cv2.Canny(gray, 25, 50)

# Find lines using Hough transform
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

# Calculate angle of each line
angles = []
for line in lines:
    x1, y1, x2, y2 = line[0]
    angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
    angles.append(angle)

# Calculate average angle
avg_angle = np.mean(angles)

print('Image angle:', avg_angle)

# Calculate image center
height, width = img.shape[:2]
center = (width // 2, height // 2)

# Calculate rotation matrix
M = cv2.getRotationMatrix2D(center, avg_angle, 1)

# Apply perspective transformation
warped = cv2.warpAffine(img, M, (width, height), flags=cv2.INTER_LINEAR)

cv2.imwrite('intermediary\\perspective4.jpg', warped)