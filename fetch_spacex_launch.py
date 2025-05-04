import requests
from download_images import download_images
import argparse
from environs import Env


def fetch_spacex_launch(path,launch_id):
    url_spacex = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url_spacex)
    response.raise_for_status()
    images_url = response.json()['links']['flickr']['original']
    if not images_url:
        print("There are not images for this launch.")
        return
    for image_index, image_url in enumerate(images_url):
        download_images(path, image_url, f'spacex_{image_index}.jpg')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch-id', type=str, default='latest')
    args = parser.parse_args()
    env = Env()
    env.read_env()
    path = env.str('IMAGE_PATH')
    fetch_spacex_launch(path, args.launch_id)


if __name__ == '__main__':
    main()