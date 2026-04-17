import allure
from jsonschema import validate

from shemas.shema_recommendations import shema_recommendation, shema_recommendations_request

BUSINESS_ID = 216704495
ENDPOINT = f'/businesses/{BUSINESS_ID}/offers/recommendations'


@allure.feature("Offers")
@allure.story("POST /businesses/{businessId}/offers/recommendations")
def test_recommendations(api):
    """Позитивный тест: Получение рекомендаций о продажах"""

    request_body = {
        "offerIds": ["example"],
        "competitivenessFilter": "OPTIMAL"
    }

    validate(request_body, schema=shema_recommendations_request)

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    body = response.json()
    assert "status" in body
    assert body["status"] == "OK", f"Статус должен быть 'OK', получен {body['status']}"
    assert "result" in body

    result = body["result"]
    assert "offerRecommendations" in result
    assert "paging" in result, "В result должен быть 'paging'"
    assert isinstance(result["offerRecommendations"], list)
    assert isinstance(result["paging"], dict)

    validate(body, schema=shema_recommendation)


@allure.feature("Offers")
@allure.story("POST /businesses/{businessId}/offers/recommendations — пустой offerIds")
def test_recommendations_empty_offer_ids(api):
    """Негативный тест: Пустой массив offerIds"""

    request_body = {
        "offerIds": [],
        "competitivenessFilter": "OPTIMAL"
    }

    response = api.post(ENDPOINT, json=request_body)

    assert response.status_code in [400, 422], \
        f"Ожидалась ошибка 400 или 422, получен {response.status_code}"

    body = response.json()
    assert body.get("status") == "ERROR", "Статус должен быть ERROR"


@allure.feature("Offers")
@allure.story("POST /businesses/{businessId}/offers/recommendations — неверный businessId")
def test_recommendations_invalid_business_id(api):
    """Негативный тест: Несуществующий businessId в URL"""

    request_body = {
        "offerIds": ["example"],
        "competitivenessFilter": "OPTIMAL"
    }

    response = api.post('/businesses/999999999/offers/recommendations', json=request_body)

    assert response.status_code in [403, 404], \
        f"Ожидался 403 или 404, получен {response.status_code}"

    body = response.json()
    assert body.get("status") == "ERROR"


@allure.feature("Offers")
@allure.story("POST /businesses/{businessId}/offers/recommendations — без авторизации")
def test_recommendations_unauthorized(api_no_auth):
    """Негативный тест: Запрос без авторизации"""

    request_body = {
        "offerIds": ["example"],
        "competitivenessFilter": "OPTIMAL"
    }

    response = api_no_auth.post(ENDPOINT, json=request_body)

    assert response.status_code in [401, 403], \
        f"Ожидался 401 или 403, получен {response.status_code}"
