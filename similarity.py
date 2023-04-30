from sewar.full_ref import mse, rmse, psnr, uqi, ergas, vifp
import cv2

blur = cv2.imread("output\\testproc2_contrast_edges_contrast_nonoise_contrast_otsu_pca_contoured_thinned.jpg")
org = cv2.imread("input\\testproc2.jpg")
print("Complet diferite")

print("MSE: ", mse(blur, org))
print("RMSE: ", rmse(blur, org))
print("PSNR: ", psnr(blur, org))
print("UQI: ", uqi(blur, org))
print("ERGAS: ", ergas(blur, org))
print("VIF: ", vifp(blur, org))


blur = cv2.imread("output\\testproc2_contrast_edges_contrast_nonoise_contrast_otsu_pca_contoured_thinned.jpg")
org = cv2.imread("output\\testproc2_contrast_edges_contrast_nonoise_contrast_otsu_pca_contoured_thinned.jpg")
print("Aceeasi poza")

print("MSE: ", mse(blur, org))
print("RMSE: ", rmse(blur, org))
print("PSNR: ", psnr(blur, org))
print("UQI: ", uqi(blur, org))
print("ERGAS: ", ergas(blur, org))
print("VIF: ", vifp(blur, org))


blur = cv2.imread("output\\testproc2_contrast_edges_contrast_nonoise_contrast_otsu_pca_contoured_thinned.jpg")
org = cv2.imread("output\\testproc3_contrast_edges_contrast_nonoise_contrast_otsu_pca_contoured_thinned.jpg")
print("2 cu 3")

print("MSE: ", mse(blur, org))
print("RMSE: ", rmse(blur, org))
print("PSNR: ", psnr(blur, org))
print("UQI: ", uqi(blur, org))
print("ERGAS: ", ergas(blur, org))
print("VIF: ", vifp(blur, org))

blur = cv2.imread("output\\testproc2_contrast_edges_contrast_nonoise_contrast_otsu_pca_contoured_thinned.jpg")
org = cv2.imread("output\\testproc3_contrast_edges_contrast_nonoise_contrast_otsu_pca_contoured_thinned.jpg")
print("2 cu 4")

print("MSE: ", mse(blur, org))
print("RMSE: ", rmse(blur, org))
print("PSNR: ", psnr(blur, org))
print("UQI: ", uqi(blur, org))
print("ERGAS: ", ergas(blur, org))
print("VIF: ", vifp(blur, org))