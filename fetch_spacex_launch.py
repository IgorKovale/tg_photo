import requests
from download_images import download_images


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