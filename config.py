import os
from dotenv import load_dotenv

load_dotenv()  # локально берёт из .env, в Jenkins из env variables

base_url = "https://api.partner.market.yandex.ru/v2"
api_key = os.getenv("API_KEY")

if not api_key:
    raise EnvironmentError("Переменная окружения API_KEY не задана")

