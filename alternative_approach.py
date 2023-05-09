import cv2
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

img1 = cv2.imread('intermediary\\cattle_0500_DSCF3908_aligned_cropped.jpg', 0)
img2 = cv2.imread('intermediary\\cattle_0500_DSCF3909_cropped.jpg', 0)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

similarity_score = cosine_similarity(des1, des2)

des1 = des1.reshape(-1, 128)
des2 = des2.reshape(-1, 128)
similarity_score = cosine_similarity(des1, des2)
similarity_percentage = int((np.mean(similarity_score) * 100).round())

print(f"The similarity between the two images is {similarity_percentage}%")