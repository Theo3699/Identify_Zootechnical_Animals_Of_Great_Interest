import cv2

# Read the input image in grayscale
img = cv2.imread('cv\\testnonostrils_sobelx1.png', 0)

# Find the contours of the binary image
contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on a copy of the original image
contour_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

# Display the resulting image
cv2.imwrite('cv\\Contours.png', contour_img)


# face ceva binisor -> sobelx apoi contour pe sobelx