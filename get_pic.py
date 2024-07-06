import requests
from PIL import Image
from io import BytesIO


def get_pic(url):
    response = requests.get(url)
    response.raise_for_status()

    image = Image.open(BytesIO(response.content))
    image.save('downloaded_image.jpg')
