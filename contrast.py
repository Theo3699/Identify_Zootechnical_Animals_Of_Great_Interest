import cv2

def enhance_contrast(file_path, input):
    print('Contrasting...')
    img = cv2.imread(file_path + input + '.jpg')

    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    # equalize the histogram of the Y channel
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

    # convert the YUV image back to RGB format
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    output = input + '_contrast'

    cv2.imwrite('intermediary\\' + output + '.jpg', img_output)
    return output