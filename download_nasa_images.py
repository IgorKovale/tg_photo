import requests
from urllib.parse import urlsplit, unquote
import os
from download_images import download_image
from environs import Env

def get_extension(url):
    url = unquote(url, encoding='utf-8', errors='replace')
    path = urlsplit(url).path
    return os.path.splitext(path)[1]

def download_nasa_images(path, nasa_key, count_of_image=5):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': f'{nasa_key}',
               'count': f'{count_of_image}'}
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    for image_index, nasa_response in enumerate(response.json()):
        nasa_image_url = nasa_response['url']
        filename = f'nasa_apod_{image_index}{get_extension(nasa_image_url)}'
        download_image(path, nasa_image_url, filename)


def main():
    env = Env()
    env.read_env()
    path = env.str('IMAGE_PATH')
    nasa_key = env.str('NASA_KEY')
    download_nasa_images(path, nasa_key)

if __name__ == '__main__':
    main()