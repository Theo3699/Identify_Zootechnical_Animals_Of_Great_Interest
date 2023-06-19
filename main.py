from blur import add_blurr
# from connect import connect_features
from contrast import enhance_contrast
from edge_detection import enhance_edges
from extract_contour import emphasize_contour
from remove_noise import remove_noise
from otsu import binarize
from pca import get_principal_components
from skeletonization import thin
from align_images import align
from nostrils import crop


def process_input(reference):
    # contrast
    # processed_image = enhance_contrast('input\\', 'cattle_0500_DSCF3909')
    # same_POV
    align(reference) # second parameter is reference
    # # remove_nostrils
    # processed_image = crop(processed_image)
    # sobel
    enhance_edges()
    # # contrast
    # processed_image = enhance_contrast('intermediary\\', processed_image)
    # # nonoise
    remove_noise()
    # blurr
    add_blurr()
    # contrast
    # processed_image = enhance_contrast('intermediary\\', processed_image)
    # otsu
    binarize()
    # connect
    # processed_image = connect_features(processed_image)
    # # pca
    # processed_image = get_principal_components(processed_image)
    # # highlight_contour
    # processed_image = emphasize_contour(processed_image)
    # # # thin
    # processed_image = thin(processed_image)