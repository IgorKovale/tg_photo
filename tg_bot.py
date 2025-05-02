import telegram
from environs import Env
import os
from time import sleep
from random import shuffle


def image_tg_chanel(path,chat_id,sleep_time):
    images = list(os.walk(fr'{path}'))[0][2]
    for image in images:
        with open(fr'{path}/{image}', 'rb') as file:
            media = telegram.InputMediaDocument(media=file)
        bot.send_media_group(chat_id=chat_id, media=[media])
        sleep(sleep_time)
    print(images)
    shuffle(images)
    i = 0
    print(images)
    while True:
        with open(fr'{path}/{image}', 'rb') as file:
            media = telegram.InputMediaDocument(media=file)
        bot.send_media_group(chat_id=chat_id, media=[media])
        sleep(sleep_time)
        i += 1


env = Env()
env.read_env()
path=env.str('IMAGE_PATH')
tg_token=env.str('TG_TOKEN')
bot = telegram.Bot(token=tg_token)
chat_id=env.str('CHAT_ID')
seconds_in_hours=3600
sleep_time=env.float('SLEEP_TIME',default=4)*seconds_in_hours
image_tg_chanel(path,chat_id,sleep_time)


