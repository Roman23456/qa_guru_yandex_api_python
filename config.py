import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://api.partner.market.yandex.ru/v2"
api_key = os.getenv("API_KEY")

campaign_id = 149032426
business_id = 216704495

if not api_key:
    raise EnvironmentError("Переменная окружения API_KEY не задана")


