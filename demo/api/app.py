import os
from PIL import Image
from pyzbar.pyzbar import decode

from flask import Flask, render_template, request

data = None
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload_qr', methods=['POST'])
def upload_qr():
    global data
    image = Image.open(request.files['image'])
    qr_codes = decode(image)
    for qr_code in qr_codes:
        data = qr_code.data.decode('utf-8')
        print('QR Code data:', data)
    return render_template('cattle_muzzle.html')


@app.route('/upload_muzzle', methods=['POST'])
def upload_muzzle():
    global data
    image = Image.open(request.files['image'])
    print(data)
    return render_template('cattle_muzzle.html')

if __name__ == '__main__':
    app.run()