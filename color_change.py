import cv2

# Load the image
img = cv2.imread('images\\testenhancednonostrils.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the Laplacian filter
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# Rescale the Laplacian output to 0-255
laplacian_rescaled = cv2.convertScaleAbs(laplacian)

# Display the result
cv2.imshow('Laplacian Filter', laplacian_rescaled)
cv2.waitKey(0)
cv2.destroyAllWindows()