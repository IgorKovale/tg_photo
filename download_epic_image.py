import requests
import datetime
from download_images import download_images
from random import sample
from environs import Env

def download_epic_image(path,nasa_api,image_count=5):
    payload = {'api_key': f'{nasa_api}'}
    url = 'https://api.nasa.gov/EPIC/api/natural/all'
    responce = requests.get(url, params=payload)
    responce.raise_for_status()
    avaible_date = sample(responce.json(),k=image_count)
    for image_index, image_date in enumerate(avaible_date):
        image_date=image_date['date']
        url = f'https://api.nasa.gov/EPIC/api/natural/date/{image_date}'
        date = datetime.date.fromisoformat(image_date)
        responce = requests.get(url, params=payload)
        responce.raise_for_status()
        image_name = responce.json()[0]['image']
        image_url = (f'https://api.nasa.gov/EPIC/archive/natural/'
                     f'{date.year:02}/{date.month:02}/{date.day:02}/png/{image_name}.png')
        download_images(path,image_url,f'epic_{image_index}.png',payload)


def main():
    env = Env()
    env.read_env()
    path = env.str('IMAGE_PATH')
    nasa_api = env.str('NASA_API')
    download_epic_image(path, nasa_api)



if __name__ == '__main__':
    main()