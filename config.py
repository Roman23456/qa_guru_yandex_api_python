import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://api.partner.market.yandex.ru/v2"
api_key = os.getenv("API_KEY")
