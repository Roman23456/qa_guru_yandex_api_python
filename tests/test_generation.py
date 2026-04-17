import allure
from jsonschema import validate

from shemas.shema_generation import shema_generation, shema_generation_request

ENDPOINT = '/reports/shows-sales/generate'


@allure.feature("Reports")
@allure.story("POST /reports/shows-sales/generate")
def test_generations(api):
    """Позитивный тест: Генерация отчёта аналитики продаж"""

    request_body = {
        "businessId": 216704495,
        "dateFrom": "2025-01-01",
        "dateTo": "2025-12-31",
        "grouping": "CATEGORIES"
    }

    validate(request_body, schema=shema_generation_request)

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert body["status"] == "OK", f"Статус в ответе должен быть OK, получен {body.get('status')}"
    assert "result" in body
    assert "reportId" in body["result"]
    assert "estimatedGenerationTime" in body["result"]
    assert isinstance(body["result"]["reportId"], str)

    validate(body, schema=shema_generation)


@allure.feature("Reports")
@allure.story("POST /reports/shows-sales/generate — несуществующий businessId")
def test_generation_invalid_business_id(api):
    """Негативный тест: Несуществующий businessId"""

    request_body = {
        "businessId": 999999999,
        "dateFrom": "2025-01-01",
        "dateTo": "2025-12-31",
        "grouping": "CATEGORIES"
    }

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code in [400, 403], \
        f"Ожидалась ошибка 400 или 403, получен {response.status_code}"

    body = response.json()
    assert body.get("status") == "ERROR", "Статус ответа должен быть ERROR"
    assert "errors" in body, "В ответе должна быть информация об ошибке"


@allure.feature("Reports")
@allure.story("POST /reports/shows-sales/generate — отсутствуют обязательные поля")
def test_generation_missing_required_fields(api):
    """Негативный тест: Отсутствует обязательное поле businessId"""

    request_body = {
        "dateFrom": "2025-01-01",
        "dateTo": "2025-12-31",
        "grouping": "CATEGORIES"
    }

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code == 400, \
        f"Ожидался 400 (Bad Request), получен {response.status_code}"

    body = response.json()
    assert body.get("status") == "ERROR"


@allure.feature("Reports")
@allure.story("POST /reports/shows-sales/generate — без авторизации")
def test_generation_unauthorized(api_no_auth):
    """Негативный тест: Запрос без авторизации"""

    request_body = {
        "businessId": 216704495,
        "dateFrom": "2025-01-01",
        "dateTo": "2025-12-31",
        "grouping": "CATEGORIES"
    }

    response = api_no_auth.post(ENDPOINT, json=request_body)

    assert response.status_code in [401, 403], \
        f"Ожидался 401 или 403, получен {response.status_code}"
