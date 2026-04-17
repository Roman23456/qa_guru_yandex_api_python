import allure
from jsonschema import validate

from schemas.schema_auth import schema_auth_token

ENDPOINT = '/auth/token'


@allure.feature("Auth")
@allure.title("Получение информации о токене")
def test_get_auth_token(api):
    response = api.post(ENDPOINT)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert body["status"] == "OK"
    assert "result" in body
    assert "apiKey" in body["result"]
    assert "Создание машин" in body["result"]["apiKey"]["name"]
    assert "ALL_METHODS" in body["result"]["apiKey"]["authScopes"]

    validate(body, schema=schema_auth_token)


@allure.feature("Auth")
@allure.title("Получение токена без авторизации — 401")
def test_get_auth_token_unauthorized(api_no_auth):
    response = api_no_auth.post(ENDPOINT)

    assert response.status_code == 401, f"Ожидался 401, получен {response.status_code}"

    body = response.json()
    assert body["status"] == "ERROR"
    assert "errors" in body

    error = body["errors"][0]
    assert error["code"] == "UNAUTHORIZED"
    assert error["message"] == "Credentials are not specified"
