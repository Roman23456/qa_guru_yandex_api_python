import allure
from jsonschema import validate

from shemas.shema_campaigns import shema_campaigns


@allure.feature("Campaigns")
@allure.story("GET /campaigns")
def test_get_campaigns(api):
    """Позитивный тест: Получение списка кампаний."""

    response = api.get('/campaigns')

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert "campaigns" in body
    assert isinstance(body["campaigns"], list)

    if len(body["campaigns"]) > 0:
        campaign = body["campaigns"][0]
        assert "id" in campaign
        assert isinstance(campaign["id"], int)
        assert "domain" in campaign or "name" in campaign, \
            "В кампании должно быть 'domain' или 'name'"
        if "business" in campaign:
            assert isinstance(campaign["business"], dict)

    assert "pager" in body
    assert "total" in body["pager"]
    assert isinstance(body["pager"]["total"], int)

    validate(body, schema=shema_campaigns)


@allure.feature("Campaigns")
@allure.story("GET /campaigns — без авторизации")
def test_campaigns_unauthorized(api_no_auth):
    """Негативный тест: Запрос без авторизации."""

    response = api_no_auth.get('/campaigns')

    assert response.status_code in [401, 403], \
        f"Ожидался 401 или 403, получен {response.status_code}"

    body = response.json()
    assert body.get("status") == "ERROR"
    assert "errors" in body


@allure.feature("Campaigns")
@allure.story("GET /campaigns — неверный Api-Key")
def test_campaigns_invalid_api_key(api_invalid_auth):
    """Негативный тест: Неверный Api-Key."""

    response = api_invalid_auth.get('/campaigns')

    assert response.status_code in [401, 403], \
        f"Ожидался 401 или 403, получен {response.status_code}"

    body = response.json()
    assert body.get("status") == "ERROR"


@allure.feature("Campaigns")
@allure.story("GET /campaigns — неверные параметры")
def test_campaigns_with_invalid_query_params(api):
    """Негативный тест: Неверные параметры запроса."""

    response = api.get('/campaigns', params={"invalidParam": "test"})
    assert response.status_code in [200, 400], \
        f"Ожидался 200 или 400, получен {response.status_code}"
