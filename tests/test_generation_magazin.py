import allure
from jsonschema import validate

from schemas.shema_generation_magazin import shema_generation_magazin, shema_generation_magazin_request

ENDPOINT = '/reports/united-netting/generate'


@allure.feature("Reports")
@allure.story("POST /reports/united-netting/generate")
def test_generations(api):
    """Позитивный тест: Генерация отчёта магазина"""

    request_body = {
        "campaignId": 149032426,
        "businessId": 216704495,
        "monthOfYear": {"year": 2026, "month": 1},
        "format": "JSON"
    }

    validate(request_body, schema=shema_generation_magazin_request)

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert body["status"] == "OK", f"Статус в ответе должен быть OK, получен {body.get('status')}"
    assert "result" in body
    assert "reportId" in body["result"]
    assert "estimatedGenerationTime" in body["result"]
    assert isinstance(body["result"]["reportId"], str)

    validate(body, schema=shema_generation_magazin)


@allure.feature("Reports")
@allure.story("POST /reports/united-netting/generate — без campaignId")
def test_generation_missing_campaign_id(api):
    """Тест: Необязательное поле campaignId может отсутствовать"""

    request_body = {
        "businessId": 216704495,
        "monthOfYear": {"year": 2026, "month": 1},
        "format": "JSON"
    }

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert body["status"] == "OK"


@allure.feature("Reports")
@allure.story("POST /reports/united-netting/generate — неверное значение месяца")
def test_generation_invalid_month_value(api):
    """Негативный тест: Месяц 13 (больше максимума)"""

    request_body = {
        "campaignId": 149032426,
        "businessId": 216704495,
        "monthOfYear": {"year": 2026, "month": 13},
        "format": "JSON"
    }

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code in [400, 422], \
        f"Ожидалась ошибка 400 или 422, получен {response.status_code}"

    body = response.json()
    assert body.get("status") == "ERROR"



@allure.feature("Reports")
@allure.story("POST /reports/united-netting/generate — без авторизации")
def test_generation_unauthorized(api_no_auth):
    """Негативный тест: Запрос без авторизации"""

    request_body = {
        "campaignId": 149032426,
        "businessId": 216704495,
        "monthOfYear": {"year": 2026, "month": 1},
        "format": "JSON"
    }

    response = api_no_auth.post(ENDPOINT, json=request_body)

    assert response.status_code in [401, 403], \
        f"Ожидался 401 или 403, получен {response.status_code}"

    body = response.json()
    assert body.get("status") == "ERROR"
