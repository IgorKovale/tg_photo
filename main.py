from environs import Env
from fetch_spacex_launch import fetch_spacex_launch
from download_nasa_image import download_nasa_image
from download_epic_image import download_epic_image
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch-id', type=str, default='latest')
    args = parser.parse_args()
    env = Env()
    env.read_env()
    path=env.str('IMAGE_PATH')
    nasa_api=env.str('NASA_API')
    # fetch_spacex_launch(path,args.launch_id)
    # download_nasa_image(path,nasa_api,count_of_image=2)
    # download_epic_image(path,nasa_api,image_count=2)
