import requests
from pathlib import Path


def download_image(path, url, filename,payload=None):
    response = requests.get(url,params=payload)
    Path(path).mkdir(parents=True, exist_ok=True)
    response.raise_for_status()
    with open(fr'{path}\{filename}', 'wb') as file:
        file.write(response.content)