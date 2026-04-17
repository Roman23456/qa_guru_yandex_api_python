import allure
from jsonschema import validate

from shemas.shema_settings import shema_campaigns

CAMPAIGN_ID = 149032426
ENDPOINT = f'/campaigns/{CAMPAIGN_ID}/settings'


@allure.feature("Settings")
@allure.story("GET /campaigns/{campaignId}/settings")
def test_get_settings_success(api):
    """Позитивный тест: Получение настроек кампании."""

    response = api.get(ENDPOINT)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert "settings" in body, "В ответе должен быть ключ 'settings'"

    settings = body["settings"]
    assert settings["countryRegion"] == 225, \
        f"countryRegion должен быть 225, а пришел {settings['countryRegion']}"
    assert settings["useOpenStat"] is False
    assert settings["shopName"] is not None

    validate(body, schema=shema_campaigns)



@allure.feature("Settings")
@allure.story("GET /campaigns/{campaignId}/settings — несуществующий campaignId")
def test_invalid_campaign_id(api):
    """Негативный тест: Несуществующий campaign ID"""

    response = api.get('/campaigns/999999999/settings')

    assert response.status_code in [403, 404], \
        f"Ожидалась ошибка 403 или 404, получен {response.status_code}"

    body = response.json()
    assert "errors" in body
    assert body.get("status") == "ERROR"


@allure.feature("Settings")
@allure.story("GET /campaigns/{campaignId}/settings — без авторизации")
def test_settings_unauthorized(api_no_auth):
    """Негативный тест: Запрос без авторизации."""

    response = api_no_auth.get(ENDPOINT)

    assert response.status_code in [401, 403], \
        f"Ожидался 401 или 403, получен {response.status_code}"

    body = response.json()
    assert body.get("status") == "ERROR"
