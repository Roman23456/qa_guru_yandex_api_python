import allure
import pytest
from jsonschema import validate

import config
from schemas.schema_united_netting import schema_united_netting, schema_united_netting_request

pytestmark = [allure.feature("Reports")]

ENDPOINT = '/reports/united-netting/generate'
REQUEST_BODY = {
    "campaignId": config.campaign_id,
    "businessId": config.business_id,
    "monthOfYear": {"year": 2026, "month": 1},
    "format": "JSON"
}


@allure.title("Генерация отчёта единого зачёта")
def test_generate_united_netting_report(api):
    validate(REQUEST_BODY, schema=schema_united_netting_request)

    response = api.post(ENDPOINT, json=REQUEST_BODY)

    if response.status_code == 420:
        pytest.skip("Rate limit: эндпоинт допускает 1 запрос в 10 минут")

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert body["status"] == "OK"
    assert isinstance(body["result"]["reportId"], str)
    assert "estimatedGenerationTime" in body["result"]

    validate(body, schema=schema_united_netting)


@allure.title("Генерация отчёта без необязательного campaignId")
def test_generate_report_without_campaign_id(api):
    body = {k: v for k, v in REQUEST_BODY.items() if k != "campaignId"}
    response = api.post(ENDPOINT, json=body)

    if response.status_code == 420:
        pytest.skip("Rate limit: эндпоинт допускает 1 запрос в 10 минут")

    assert response.status_code == 200
    assert response.json()["status"] == "OK"


@allure.title("Генерация отчёта с неверным значением месяца (13)")
def test_generate_report_invalid_month(api):
    body = {**REQUEST_BODY, "monthOfYear": {"year": 2026, "month": 13}}
    response = api.post(ENDPOINT, json=body)

    if response.status_code == 420:
        pytest.skip("Rate limit: эндпоинт допускает 1 запрос в 10 минут")

    assert response.status_code == 400
    assert response.json().get("status") == "ERROR"


@allure.title("Генерация отчёта без авторизации")
def test_generate_report_unauthorized(api_no_auth):
    response = api_no_auth.post(ENDPOINT, json=REQUEST_BODY)

    assert response.status_code in [401]
    assert response.json().get("status") == "ERROR"
