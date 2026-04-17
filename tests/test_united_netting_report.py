import allure
from jsonschema import validate

from schemas.schema_united_netting import schema_united_netting, schema_united_netting_request

ENDPOINT = '/reports/united-netting/generate'


@allure.feature("Reports")
@allure.title("Генерация отчёта единого зачёта")
def test_generate_united_netting_report(api):
    request_body = {
        "campaignId": 149032426,
        "businessId": 216704495,
        "monthOfYear": {"year": 2026, "month": 1},
        "format": "JSON"
    }

    validate(request_body, schema=schema_united_netting_request)

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert body["status"] == "OK"
    assert "reportId" in body["result"]
    assert "estimatedGenerationTime" in body["result"]
    assert isinstance(body["result"]["reportId"], str)

    validate(body, schema=schema_united_netting)


@allure.feature("Reports")
@allure.title("Генерация отчёта без необязательного campaignId — 200")
def test_generate_report_without_campaign_id(api):
    request_body = {
        "businessId": 216704495,
        "monthOfYear": {"year": 2026, "month": 1},
        "format": "JSON"
    }

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code == 200
    assert response.json()["status"] == "OK"


@allure.feature("Reports")
@allure.title("Генерация отчёта с неверным значением месяца (13) — 400/422")
def test_generate_report_invalid_month(api):
    request_body = {
        "campaignId": 149032426,
        "businessId": 216704495,
        "monthOfYear": {"year": 2026, "month": 13},
        "format": "JSON"
    }

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code in [400, 422]
    assert response.json().get("status") == "ERROR"


@allure.feature("Reports")
@allure.title("Генерация отчёта без авторизации — 401/403")
def test_generate_report_unauthorized(api_no_auth):
    request_body = {
        "campaignId": 149032426,
        "businessId": 216704495,
        "monthOfYear": {"year": 2026, "month": 1},
        "format": "JSON"
    }

    response = api_no_auth.post(ENDPOINT, json=request_body)

    assert response.status_code in [401, 403]
    assert response.json().get("status") == "ERROR"
