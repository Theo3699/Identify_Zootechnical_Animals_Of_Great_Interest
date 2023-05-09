from blur import add_blurr
from connect import connect_features
from contrast import enhance_contrast
from edge_detection import enhance_edges
from extract_contour import emphasize_contour
from remove_noise import remove_noise
from otsu import binarize
from pca import get_principal_components
from skeletonization import thin
from align_images import align
from nostrils import crop


if __name__ == '__main__':
    # contrast
    # processed_image = enhance_contrast('input\\', 'cattle_0500_DSCF3909')
    # same_POV
    # processed_image = align('cattle_0500_DSCF3908', 'cattle_0500_DSCF3909') # second parameter is reference
    # # remove_nostrils
    # processed_image = crop(processed_image)
    # sobel
    processed_image = enhance_edges('cattle_1400_DSCF4014')
    # # contrast
    # processed_image = enhance_contrast('intermediary\\', processed_image)
    # # nonoise
    processed_image = remove_noise(processed_image)
    # blurr
    processed_image = add_blurr(processed_image)
    # contrast
    # processed_image = enhance_contrast('intermediary\\', processed_image)
    # otsu
    processed_image = binarize(processed_image)
    # connect
    # processed_image = connect_features(processed_image)
    # # pca
    # processed_image = get_principal_components(processed_image)
    # # highlight_contour
    # processed_image = emphasize_contour(processed_image)
    # # # thin
    # processed_image = thin(processed_image)