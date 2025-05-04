import requests
from download_images import download_image
import argparse
from environs import Env


def fetch_spacex_launch(path,launch_id):
    spacex_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(spacex_url)
    response.raise_for_status()
    images_url = response.json()['links']['flickr']['original']
    if not images_url:
        print("There are not images for this launch.")
        return
    for image_index, image_url in enumerate(images_url):
        download_image(path, image_url, f'spacex_{image_index}.jpg')


def main():
    parser = argparse.ArgumentParser(description="Загружает фотографии запуска spacex")
    parser.add_argument('--launch_id', help="id запуска,"
                                           " по умолчанию стоит последний запуск", type=str, default='latest')
    args = parser.parse_args()
    env = Env()
    env.read_env()
    path = env.str('IMAGE_PATH')
    fetch_spacex_launch(path, args.launch_id)


if __name__ == '__main__':
    main()