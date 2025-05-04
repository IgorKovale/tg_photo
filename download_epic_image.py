import requests
import datetime
from download_images import download_image
from random import sample
from environs import Env

def download_epic_images(path, nasa_key, image_count=5):
    payload = {'api_key': f'{nasa_key}'}
    url = 'https://api.nasa.gov/EPIC/api/natural/all'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    available_date = sample(response.json(),k=image_count)
    for image_index, image_date in enumerate(available_date):
        image_date=image_date['date']
        url = f'https://api.nasa.gov/EPIC/api/natural/date/{image_date}'
        date = datetime.date.fromisoformat(image_date)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        image_name = response.json()[0]['image']
        image_url = (f'https://api.nasa.gov/EPIC/archive/natural/'
                     f'{date.year:02}/{date.month:02}/{date.day:02}/png/{image_name}.png')
        download_image(path,image_url,f'epic_{image_index}.png',payload)


def main():
    env = Env()
    env.read_env()
    path = env.str('IMAGE_PATH')
    nasa_key = env.str('NASA_KEY')
    download_epic_images(path, nasa_key)



if __name__ == '__main__':
    main()