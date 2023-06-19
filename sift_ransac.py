import cv2
import numpy as np

# Set the maximum allowed reprojection error
MAX_REPROJECTION_ERROR = 5.0

def ransac_filter(matches, keypoints1, keypoints2):
    """
    Apply RANSAC to filter good matches.

    Args:
        matches: list of DMatch objects representing the matches
        keypoints1: list of KeyPoint objects representing the keypoints in the first image
        keypoints2: list of KeyPoint objects representing the keypoints in the second image

    Returns:
        list of DMatch objects representing the filtered matches
    """
    # Convert keypoints to numpy arrays
    pts1 = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    pts2 = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    # Apply RANSAC to find the best matches
    _, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, MAX_REPROJECTION_ERROR)
    mask = mask.ravel().tolist()

    # Filter the matches based on the RANSAC mask
    filtered_matches = []
    for i, match in enumerate(matches):
        if mask[i]:
            filtered_matches.append(match)

    return filtered_matches

def calculate_similarity():
    # Load the images
    img1 = cv2.imread('C:\\Users\\Theo\\PycharmProjects\\pythonProject\\demo\\api\\final\\input_aligned_edges_nonoise_blurred_otsu.jpg')
    img2 = cv2.imread('C:\\Users\\Theo\\PycharmProjects\\pythonProject\\demo\\api\\mock_database\\cattle_0100_DSCF3865_edges_nonoise_blurred_otsu.jpg') # reference

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
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)


    filtered_matches = ransac_filter(good_matches, kp1, kp2)
    result = cv2.drawMatches(img1, kp1, img2, kp2, filtered_matches, None)

    result_path = 'C:\\Users\\Theo\\PycharmProjects\\pythonProject\\demo\\api\\result\\similarity.jpg'
    cv2.imwrite(result_path, result)

    print('Most relevant matches:', len(filtered_matches))
    return result_path