import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import cv2
import numpy as np

# Load the input image
input_image = cv2.imread("output\\connectedpca.png")

data = np.reshape(input_image, (-1, 3))

# Use t-SNE to reduce the dimensionality of the data to 2D
tsne = TSNE(n_components=2, perplexity=30, verbose=1)
tsne_result = tsne.fit_transform(data)

# Plot the t-SNE results
plt.scatter(tsne_result[:,0], tsne_result[:,1])
plt.show()