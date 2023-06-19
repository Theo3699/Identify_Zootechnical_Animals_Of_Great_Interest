import os
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from main import process_input
from sift_ransac import calculate_similarity
import json

from flask import Flask, render_template, request, send_file

data = None
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload_qr', methods=['POST'])
def upload_qr():
    global data
    image = request.files['image']
    image_array = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    qr_codes = decode(image_array)
    for qr_code in qr_codes:
        data = qr_code.data.decode('utf-8')
        print('QR Code data:', data)
    return render_template('cattle_muzzle.html')


@app.route('/upload_muzzle', methods=['POST'])
def upload_muzzle():
    global data
    image = request.files['image']
    image.save("C:\\Users\\Theo\\PycharmProjects\\pythonProject\\demo\\api\\input\\input.jpg")

    data = json.loads(data)

    # send as image the reference from the qr mock database
    folder_path = "references\\"

    # Iterate over all files in the qr mock database
    counter = 1
    for filename in os.listdir(folder_path):
        if counter == int(data["reference_image_index"]):
            reference_path = os.path.join(folder_path, filename)
            break
        counter += 1
    process_input(reference_path)
    result = calculate_similarity()
    return send_file(result, mimetype="image/jpg")

if __name__ == '__main__':
    app.run()