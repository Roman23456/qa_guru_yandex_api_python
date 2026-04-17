import allure
from jsonschema import validate

from schemas.schema_shows_sales import schema_shows_sales, schema_shows_sales_request

ENDPOINT = '/reports/shows-sales/generate'


@allure.feature("Reports")
@allure.title("Генерация отчёта аналитики продаж")
def test_generate_shows_sales_report(api):
    request_body = {
        "businessId": 216704495,
        "dateFrom": "2025-01-01",
        "dateTo": "2025-12-31",
        "grouping": "CATEGORIES"
    }

    validate(request_body, schema=schema_shows_sales_request)

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert body["status"] == "OK"
    assert "reportId" in body["result"]
    assert "estimatedGenerationTime" in body["result"]
    assert isinstance(body["result"]["reportId"], str)

    validate(body, schema=schema_shows_sales)


@allure.feature("Reports")
@allure.title("Генерация отчёта с несуществующим businessId — 400/403")
def test_generate_report_invalid_business_id(api):
    request_body = {
        "businessId": 999999999,
        "dateFrom": "2025-01-01",
        "dateTo": "2025-12-31",
        "grouping": "CATEGORIES"
    }

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code in [400, 403]

    body = response.json()
    assert body.get("status") == "ERROR"
    assert "errors" in body


@allure.feature("Reports")
@allure.title("Генерация отчёта без обязательного поля businessId — 400")
def test_generate_report_missing_business_id(api):
    request_body = {
        "dateFrom": "2025-01-01",
        "dateTo": "2025-12-31",
        "grouping": "CATEGORIES"
    }

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code == 400
    assert response.json().get("status") == "ERROR"


@allure.feature("Reports")
@allure.title("Генерация отчёта без авторизации — 401/403")
def test_generate_report_unauthorized(api_no_auth):
    request_body = {
        "businessId": 216704495,
        "dateFrom": "2025-01-01",
        "dateTo": "2025-12-31",
        "grouping": "CATEGORIES"
    }

    response = api_no_auth.post(ENDPOINT, json=request_body)

    assert response.status_code in [401, 403]
