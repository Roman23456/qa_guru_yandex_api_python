import allure
from jsonschema import validate

from shemas.shema_information import shema_token

ENDPOINT = '/auth/token'


@allure.feature("Auth")
@allure.story("POST /auth/token")
def test_information_token(api):
    """Позитивный тест: Получение информации о токене"""

    response = api.post(ENDPOINT)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert body["status"] == "OK", "Статус в теле ответа должен быть OK"
    assert "result" in body
    assert "apiKey" in body["result"]
    assert "Создание машин" in body["result"]["apiKey"]["name"]
    assert "ALL_METHODS" in body["result"]["apiKey"]["authScopes"]

    validate(body, schema=shema_token)



@allure.feature("Auth")
@allure.story("POST /auth/token — без авторизации")
def test_failed_token_no_api_key(api_no_auth):
    """Негативный тест: Без Api-Key возвращается 401"""

    response = api_no_auth.post(ENDPOINT)

    assert response.status_code == 401, f"Ожидался 401, получен {response.status_code}"

    body = response.json()
    assert body["status"] == "ERROR"
    assert "errors" in body
    assert len(body["errors"]) > 0

    error = body["errors"][0]
    assert error["code"] == "UNAUTHORIZED", \
        f"Ожидался код UNAUTHORIZED, получен {error['code']}"
    assert error["message"] == "Credentials are not specified", \
        f"Неверное сообщение: {error['message']}"
