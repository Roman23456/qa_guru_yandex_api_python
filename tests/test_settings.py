import allure
import pytest
from jsonschema import validate

import config
from schemas.schema_settings import schema_settings

pytestmark = [allure.feature("Settings")]

ENDPOINT = f'/campaigns/{config.campaign_id}/settings'


@allure.title("Получение настроек кампании")
def test_get_settings(api):
    response = api.get(ENDPOINT)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert "settings" in body

    settings = body["settings"]
    assert settings["countryRegion"] == 225
    assert settings["useOpenStat"] is False
    assert settings["shopName"] is not None

    validate(body, schema=schema_settings)


@allure.title("Получение настроек с несуществующим campaignId — 403/404")
def test_get_settings_invalid_campaign_id(api):
    response = api.get('/campaigns/999999999/settings')

    assert response.status_code in [403, 404]

    body = response.json()
    assert body.get("status") == "ERROR"
    assert "errors" in body


@allure.title("Получение настроек без авторизации — 401/403")
def test_get_settings_unauthorized(api_no_auth):
    response = api_no_auth.get(ENDPOINT)

    assert response.status_code in [401, 403]
    assert response.json().get("status") == "ERROR"
