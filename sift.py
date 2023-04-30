import cv2

# Load the two images to compare
img1 = cv2.imread('images\\test.jpg')
img2 = cv2.imread('images\\testenhanced.png')

# Preprocess the images
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Initialize the SIFT feature detector and descriptor extractor
sift = cv2.xfeatures2d.SIFT_create()

# Detect keypoints and compute descriptors for each image
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# Initialize the feature matcher
bf = cv2.BFMatcher()

# Match descriptors between the two images
matches = bf.knnMatch(des1, des2, k=2)

# Apply ratio test to remove ambiguous matches
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# Compute the similarity score based on the number of good matches
score = len(good_matches) / min(len(kp1), len(kp2))

# Print the similarity score
print('Similarity score:', score)