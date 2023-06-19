import cv2
import numpy as np


def align(reference):
    print('Aligning reference photo with input photo...')
    # Load the images
    input_path = 'C:\\Users\\Theo\\PycharmProjects\\pythonProject\\demo\\api\\input\\input.jpg'
    img1 = cv2.imread(input_path)
    img2 = cv2.imread('C:\\Users\\Theo\\PycharmProjects\\pythonProject\\demo\\api\\' + reference) # reference

    # Convert the images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Create a SIFT feature detector
    sift = cv2.xfeatures2d.SIFT_create()

    # Detect key points and descriptors in both images
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    # Match the key points in the two images
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply Lowe's ratio test to filter matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Extract the key points from the good matches
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # Estimate the transformation matrix using RANSAC
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    # Apply the transformation matrix to the first image
    aligned_img1 = cv2.warpPerspective(img1, M, (img2.shape[1], img2.shape[0]))

    # Crop the aligned images to remove any black borders
    aligned_img1 = cv2.copyMakeBorder(aligned_img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    x, y, w, h = cv2.boundingRect(cv2.cvtColor(aligned_img1, cv2.COLOR_BGR2GRAY))
    aligned_img1 = aligned_img1[y:y+h, x:x+w]

    output = 'C:\\Users\\Theo\\PycharmProjects\\pythonProject\\demo\\api\\intermediary\\input_aligned.jpg'
    # Display the aligned images
    cv2.imwrite(output, aligned_img1)
    return output