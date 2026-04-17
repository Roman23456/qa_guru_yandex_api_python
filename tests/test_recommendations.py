import allure
from jsonschema import validate

import config
from schemas.schema_recommendations import schema_recommendation, schema_recommendations_request

pytestmark = [allure.feature("Offers")]

ENDPOINT = f'/businesses/{config.business_id}/offers/recommendations'


@allure.title("Получение рекомендаций по товарам")
def test_get_recommendations(api):
    request_body = {
        "offerIds": ["example"],
        "competitivenessFilter": "OPTIMAL"
    }

    validate(request_body, schema=schema_recommendations_request)

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert body["status"] == "OK"
    assert "result" in body

    result = body["result"]
    assert isinstance(result["offerRecommendations"], list)
    assert isinstance(result["paging"], dict)

    validate(body, schema=schema_recommendation)


@allure.title("Получение рекомендаций с пустым списком offerIds — 400/422")
def test_get_recommendations_empty_offer_ids(api):
    response = api.post(ENDPOINT, json={"offerIds": [], "competitivenessFilter": "OPTIMAL"})

    assert response.status_code in [400, 422]
    assert response.json().get("status") == "ERROR"



@allure.title("Получение рекомендаций с несуществующим businessId — 403/404")
def test_get_recommendations_invalid_business_id(api):
    response = api.post(
        '/businesses/999999999/offers/recommendations',
        json={"offerIds": ["example"], "competitivenessFilter": "OPTIMAL"}
    )

    assert response.status_code in [403, 404]
    assert response.json().get("status") == "ERROR"


@allure.title("Получение рекомендаций без авторизации — 401/403")
def test_get_recommendations_unauthorized(api_no_auth):
    response = api_no_auth.post(
        ENDPOINT,
        json={"offerIds": ["example"], "competitivenessFilter": "OPTIMAL"}
    )

    assert response.status_code in [401, 403]
