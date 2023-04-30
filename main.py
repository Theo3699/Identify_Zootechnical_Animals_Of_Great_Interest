from contour2 import draw_contour
from contrast import enhance_contrast
from edge_detection import enhance_edges
from extract_contour import emphasize_contour
from remove_noise import remove_noise
from otsu import binarize
from pca import get_principal_components
from skeletonization import thin
from align_images import align
from nostrils import crop

# nu merge sift aligned cu alte animale decat cu cel de referinta sa-l alinieze
if __name__ == '__main__':
    # contrast
    processed_image = enhance_contrast('input\\', 'cattle_0200_DSCF3870')
    # same_POV
    processed_image = align(processed_image, 'cattle_0600_DSCF3919_contrast') # second parameter is reference
    # remove_nostrils
    processed_image = crop(processed_image)
    # sobel_x
    processed_image = enhance_edges(processed_image)
    # contrast
    processed_image = enhance_contrast('intermediary\\', processed_image)
    # nonoise
    processed_image = remove_noise(processed_image)
    # contrast
    processed_image = enhance_contrast('intermediary\\', processed_image)
    # otsu
    processed_image = binarize(processed_image)
    # # contour
    # processed_image = draw_contour(processed_image)
    # pca
    processed_image = get_principal_components(processed_image)
    # highlight_contour
    processed_image = emphasize_contour(processed_image)
    # thin
    processed_image = thin(processed_image)