import telegram
from environs import Env


env = Env()
env.read_env()
tg_token=env.str('TG_TOKEN')
bot = telegram.Bot(token=tg_token)
print(bot.get_me())
chat_id=env.str('CHAT_ID')
bot.send_message(chat_id=chat_id, text="message")
