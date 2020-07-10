#!/usr/bin/python3
"""
    Just a routine practice: working with images.
"""
from PIL import Image
import requests
from io import BytesIO

image_url = 'http://cdn29.us1.fansshare.com/pictures/fairytail/image-fairy-tail-happy-fairy-tail-by-ichigo-op-big-happy-76012260.jpg'


# Resize the image
def img_resize(img):
    width, height = img.size
    print(f'Resize to width:{int(width / 2)} and height:{int(height / 2)}')
    img = img.resize((int(width * 2), int(height * 2)))
    img.show()


# Crop the image
def img_crop(img):
    width, height = img.size
    print(f'Crop from  width:{width} and height:{height} to width:{width / 5} and height:{height / 5}')
    img = img.crop((0, 0, width / 2, height / 2))
    img.show()


# Save the image
def save_image(img, name_image):
    img.save(name_image)


if __name__ == '__main__':
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    print(f'Image original Size:{img.size} - image format:{img.format_description}')
    img.show()
    img_resize(img)
    img_crop(img)
    save_image(img, "test_dj.jpg")
