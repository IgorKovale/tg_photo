import requests
from urllib.parse import urlsplit, unquote
import os
from download_images import download_images

def get_extension(url):
    url = unquote(url, encoding='utf-8', errors='replace')
    path = urlsplit(url).path
    return os.path.splitext(path)[1]

def download_nasa_image(path,nasa_api,count_of_image=5):
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': f'{nasa_api}',
               'count': f'{count_of_image}'}
    response = requests.get(url_nasa, params=payload)
    response.raise_for_status()
    for image_index, nasa_response in enumerate(response.json()):
        nasa_image_url = nasa_response['url']
        filename = f'nasa_apod_{image_index}{get_extension(nasa_image_url)}'
        download_images(path, nasa_image_url, filename)