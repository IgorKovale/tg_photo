import telegram
from environs import Env


env = Env()
env.read_env()
tg_token=env.str('TG_TOKEN')
bot = telegram.Bot(token=tg_token)
chat_id=env.str('CHAT_ID')
with open('image/nasa_apod_0.jpg', 'rb') as file:
    media_1 = telegram.InputMediaDocument(media=file)
bot.send_media_group(chat_id=chat_id, media=[media_1])
