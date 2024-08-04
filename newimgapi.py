from flask import Flask, send_file
import requests
import numpy as np
import cv2
from io import BytesIO
from PIL import Image

app = Flask(__name__)


def get_image_url():

    access_key = '45122305-ff67b78c9623bb9c382f1628b'
    url = f'https://pixabay.com/api/?key=45122305-ff67b78c9623bb9c382f1628b&q=yellow+flowers&image_type=photo&pretty=true{access_key}'
    response = requests.get(url)
    data = response.json()
    image_url = data['https://cdn.pixabay.com/user/2013/11/05/02-10-23-764_250x250.jpg']['regular']
    return image_url

def download_image(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image

@app.route('/get')
def display_image():
    image_url = get_image_url('https://pixabay.com/photos/stamens-botany-macro-photography-6472927/')
    image = download_image(image_url)
    
    # Save the image to a temporary file
    is_success, buffer = cv2.imencode(".jpg", image)
    io_buf = BytesIO(buffer)
    
    return send_file(io_buf, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
