"""
    Author: Altair
    Date: 2022-02-14 (Happy Valentine's Day)
    Description:
        Some BS about jetson, who cares.

"""


from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

IMAGES_DIR = "static/images"

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

PORT = 6969


@app.after_request
def add_header(response):

    response.headers['cache-control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route('/ping')
def ping():

    return jsonify({"Talha": "Altair"})


@app.route('/')
def index():

    images = list_images()

    return render_template('index.html', images=images, images_dir=IMAGES_DIR)


@app.route('/fetch/images')
def fetch_images():

    images = list_images()

    data = {
        "images": images
    }

    return jsonify(data)


def list_images():

    images = os.listdir(IMAGES_DIR)

    images = [image for image in images if image.split(
        '.')[-1] in ALLOWED_EXTENSIONS]

    return images


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=PORT)
