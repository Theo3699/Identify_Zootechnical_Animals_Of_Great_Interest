
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
import cv2
import matplotlib.pyplot as plt

img = imread('images\\connected.png')
plt.axis("off")
plt.imshow(img)
print(img.shape)


resized_img = resize(img, (128*4, 64*4))
plt.axis("off")
plt.imshow(resized_img)
print(resized_img.shape)


fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True, channel_axis=2)
cv2.imwrite('images\\hog.png', 255*hog_image)