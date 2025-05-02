# Загрузка изображений NASA и SpaceX
Проект предназначен для автоматической загрузки
изображений с API NASA и SpaceX и сохранения их в
указанной папке.
## Описание функций
- Загрузка изображений запуска SpaceX
- Скачивание ежедневных фотографий программы APOD (Astronomy Picture of the Day) от NASA
- Скачивание фото Земли из программы EPIC (Earth Polychromatic Imaging Camera)
## Требования
Python >= 3.7
Библиотеки: `requests`, `datetime`, `environs`, `python-telegram-bot==13.0`
## Установка
Клонируйте репозиторий и установите необходимые зависимости:
```bash
pip install -r requirements.txt
```
Создайте файл `.env` и добавьте туда:
|Имя переменной|Описание|
|---|--|
NASA_API|	Ключ API для доступа к службам NASA.
IMAGE_PATH|	Путь к папке с изображениями, используемыми в проекте.
TG_TOKEN	Токен для доступа к Telegram API (используется для взаимодействия с ботом).
CHAT_ID	Идентификатор чата Telegram, куда отправляются уведомления или сообщения.
TIME_SLEEP	Интервал ожидания (в секундах) между последовательными действиями.
NASA_API=ваш апи с сайта 
IMAGE_PATH=C:/Folder/Scriptss/devman_lessons/tg_photo/image
TG_TOKEN=8156702401:AAEYODI4oACPomYXsEXezX_ZvxWksyhka_k
CHAT_ID='@test_image_downloader'
TIME_SLEEP=4
```bash
IMAGE_PATH="./images/"
NASA_API="your-nasa-api-key-here"
```
## Запуск
Скрипт запускается следующим образом:
```bash
python main.py
```
По завершении работы программа скачает изображения и сохранит их в указанную директорию.

