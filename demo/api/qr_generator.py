import qrcode

data = '{' \
       '"farm_id": "RO123456789",' \
       '"breed": "Holstein",' \
       '"reference_image_index": "2"' \
       '}'
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

qr_image = qr.make_image(fill_color='black', back_color='white')

image_path = 'qrs/qr_demo_2_input2.png'  # Replace with the path to save the image
qr_image.save(image_path)