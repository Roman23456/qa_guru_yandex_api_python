import allure
from jsonschema import validate

import config
from schemas.schema_shows_sales import schema_shows_sales, schema_shows_sales_request

pytestmark = [allure.feature("Reports")]

ENDPOINT = '/reports/shows-sales/generate'
REQUEST_BODY = {
    "businessId": config.business_id,
    "dateFrom": "2026-04-01",
    "dateTo": "2026-05-01",
    "grouping": "CATEGORIES"
}


@allure.title("Генерация отчёта аналитики продаж")
def test_generate_shows_sales_report(api):
    validate(REQUEST_BODY, schema=schema_shows_sales_request)

    response = api.post(ENDPOINT, json=REQUEST_BODY)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert body["status"] == "OK"
    assert isinstance(body["result"]["reportId"], str)
    assert "estimatedGenerationTime" in body["result"]

    validate(body, schema=schema_shows_sales)


@allure.title("Генерация отчёта с несуществующим businessId")
def test_generate_report_invalid_business_id(api):
    response = api.post(ENDPOINT, json={**REQUEST_BODY, "businessId": 999999999})

    # API допускает не более 1 запроса в 10 минут на этот эндпоинт, при превышении возвращает 420
    assert response.status_code in [403, 420]

    body = response.json()
    assert body.get("status") == "ERROR"
    assert "errors" in body


@allure.title("Генерация отчёта без обязательного поля businessId")
def test_generate_report_missing_business_id(api):
    body = {k: v for k, v in REQUEST_BODY.items() if k != "businessId"}
    response = api.post(ENDPOINT, json=body)

    # API допускает не более 1 запроса в 10 минут на этот эндпоинт, при превышении возвращает 420
    assert response.status_code in [400, 420]
    assert response.json().get("status") == "ERROR"


@allure.title("Генерация отчёта без авторизации")
def test_generate_report_unauthorized(api_no_auth):
    response = api_no_auth.post(ENDPOINT, json=REQUEST_BODY)

    assert response.status_code == 401
