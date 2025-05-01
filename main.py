import requests
from urllib.parse import urlparse, urlsplit, unquote
import os
import datetime
from environs import Env
from pathlib import Path

def download_images(path, url, filename,payload=None):
    response = requests.get(url,params=payload)
    Path(path).mkdir(parents=True, exist_ok=True)
    response.raise_for_status()
    with open(fr'{path}\{filename}', 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch(path,launch_id):
    url_spacex = 'https://api.spacexdata.com/v5/launches'
    response = requests.get(url_spacex)
    response.raise_for_status()
    images_url = response.json()[launch_id]['links']['flickr']['original']
    for image_index, image_url in enumerate(images_url):
        download_images(path, image_url, f'spacex_{image_index}.jpg')

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


def download_epic_image(path,nasa_api,image_count=5):
    payload = {'api_key': f'{nasa_api}'}
    url = 'https://api.nasa.gov/EPIC/api/natural/all'
    responce = requests.get(url, params=payload)
    responce.raise_for_status()
    avaible_date = responce.json()[:image_count]
    for image_index, image_date in enumerate(avaible_date):
        url = f'https://api.nasa.gov/EPIC/api/natural/date/{image_date['date']}'
        date = datetime.date.fromisoformat(image_date['date'])
        responce = requests.get(url, params=payload)
        responce.raise_for_status()
        image_name = responce.json()[0]['image']
        image_url = (f'https://api.nasa.gov/EPIC/archive/natural/'
                     f'{date.year:02}/{date.month:02}/{date.day:02}/png/{image_name}.png')
        download_images(path,image_url,f'epic_{image_index}.png',payload)

if __name__ == "__main__":
    env = Env()
    env.read_env()
    path=env.str('IMAGE_PATH')
    nasa_api=env.str('NASA_API')
    download_epic_image(path,nasa_api)
    download_nasa_image(path,nasa_api)
    fetch_spacex_launch(path,25)
