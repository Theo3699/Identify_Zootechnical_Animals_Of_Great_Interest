from sewar.full_ref import mse, rmse, psnr, uqi, ergas, vifp
import cv2

def get_similarity(img1, img2):
    print("MSE: ", mse(img1, img2))
    print("RMSE: ", rmse(img1, img2))
    print("PSNR: ", psnr(img1, img2))
    print("UQI: ", uqi(img1, img2))
    print("ERGAS: ", ergas(img1, img2))


def reshape(img1, img2):
    height = 2400
    width = 1800
    img1_resized = cv2.resize(img1, (width, height))
    img2_resized = cv2.resize(img2, (width, height))
    return img1_resized, img2_resized


# img1 = cv2.imread("output\\cattle_0300_DSCF3890_contrast_aligned_cropped_edges_contrast_nonoise_contrast_otsu_pca_contoured_thinned.jpg")
# img2 = cv2.imread("output\\cattle_0400_DJI_0129_contrast_aligned_cropped_edges_contrast_nonoise_contrast_otsu_pca_contoured_thinned.jpg")
# img1, img2 = reshape(img1, img2)
# print("Vaci diferite")
#
# get_similarity(img1, img2)
#
#
#
# img1 = cv2.imread("output\\cattle_0300_DJI_0122_contrast_aligned_cropped_edges_contrast_nonoise_contrast_otsu_pca_contoured_thinned.jpg")
# img2 = cv2.imread("output\\cattle_0400_DJI_0129_contrast_aligned_cropped_edges_contrast_nonoise_contrast_otsu_pca_contoured_thinned.jpg")
# img1, img2 = reshape(img1, img2)
# print("Vaci diferite")
#
# get_similarity(img1, img2)
#
#
#
img1 = cv2.imread("output\\cattle_0500_DSCF3908_edges_nonoise_blurred_otsu_connected.jpg")
img2 = cv2.imread("output\\cattle_0500_DSCF3909_edges_nonoise_blurred_otsu_connected.jpg")
img1, img2 = reshape(img1, img2)
print("Aceeasi vaca")

get_similarity(img1, img2)


# import numpy as np
#
# img1 = cv2.imread("intermediary\\cattle_0500_DSCF3908_edges_nonoise_blurred_otsu.jpg")
# img2 = cv2.imread("intermediary\\cattle_0500_DSCF3909_edges_nonoise_blurred_otsu.jpg")
# img1, img2 = reshape(img1, img2)
#
# #--- take the absolute difference of the images ---
# res = cv2.absdiff(img1, img2)
#
# #--- convert the result to integer type ---
# res = res.astype(np.uint8)
#
# #--- find percentage difference based on number of pixels that are not zero ---
# percentage = (np.count_nonzero(res) * 100)/ res.size
# print(percentage)