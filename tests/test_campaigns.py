import allure
from jsonschema import validate

from schemas.schema_campaigns import schema_campaigns

pytestmark = [allure.feature("Campaigns")]


@allure.title("Получение списка кампаний")
def test_get_campaigns(api):
    response = api.get('/campaigns')

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert "campaigns" in body
    assert isinstance(body["campaigns"], list)

    if body["campaigns"]:
        campaign = body["campaigns"][0]
        assert "id" in campaign
        assert isinstance(campaign["id"], int)
        assert "domain" in campaign or "name" in campaign
        if "business" in campaign:
            assert isinstance(campaign["business"], dict)

    assert "pager" in body
    assert isinstance(body["pager"]["total"], int)

    validate(body, schema=schema_campaigns)


@allure.title("Получение кампаний без авторизации")
def test_get_campaigns_unauthorized(api_no_auth):
    response = api_no_auth.get('/campaigns')

    assert response.status_code == 401

    body = response.json()
    assert body.get("status") == "ERROR"
    assert "errors" in body


@allure.title("Получение кампаний с неверным Api-Key")
def test_get_campaigns_invalid_api_key(api_invalid_auth):
    response = api_invalid_auth.get('/campaigns')

    assert response.status_code == 401
    assert response.json().get("status") == "ERROR"


@allure.title("Получение кампаний с неизвестными параметрами")
def test_get_campaigns_unknown_params(api):
    response = api.get('/campaigns', params={"unknownParam": "test"})

    assert response.status_code == 200

