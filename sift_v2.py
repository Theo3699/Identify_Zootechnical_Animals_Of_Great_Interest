import math

import cv2

print('Calculating similarity score...')
# Load the images
img1 = cv2.imread("intermediary\\cattle_0500_DSCF3908_aligned_edges_nonoise_blurred_otsu.jpg")
img2 = cv2.imread("intermediary\\cattle_0500_DSCF3909_edges_nonoise_blurred_otsu.jpg") # reference

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


# Compute the angle of each keypoint
angles1 = [kp.angle for kp in kp1]
angles2 = [kp.angle for kp in kp2]


# Filter the matches based on the difference in angle
angle_threshold = math.radians(10)  # Set a threshold for the angle difference (15 degrees)
horizontal_matches = []
for m in good_matches:
    angle_diff = abs(angles1[m.queryIdx] - angles2[m.trainIdx])
    if angle_diff < angle_threshold or angle_diff > math.pi - angle_threshold:
        horizontal_matches.append(m)


# Draw the matches
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, horizontal_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Compute the similarity score based on the number of good matches
score = len(horizontal_matches) / min(len(kp1), len(kp2)) * 1000

# Print the similarity score
print('Similarity score:', score, '%')

# Display the matches
cv2.imwrite('Matches.jpg', img_matches)