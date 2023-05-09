import cv2

img = cv2.imread('intermediary\\cattle_0500_DSCF3908_contrast.jpg',0)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

sobel = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)

cv2.imwrite('sobel.jpg', sobel)