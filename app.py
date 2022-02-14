from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

IMAGES_DIR = "static/images"


@app.route('/ping')
def ping():

    return jsonify({"ping": "pong"})


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

    return images


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=6969)
