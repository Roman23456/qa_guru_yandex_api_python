import allure
from jsonschema import validate

from shemas.shema_outlets import shema_outlet_error

CAMPAIGN_ID = 149032426


@allure.feature("Outlets")
@allure.story("DELETE /campaigns/{campaignId}/outlets/{outletId} — несуществующий outlet")
def test_delete_outlet_not_found(api):
    """Негативный тест: Удаление несуществующей точки выдачи"""

    response = api.delete(f'/campaigns/{CAMPAIGN_ID}/outlets/999999999')

    assert response.status_code in [400, 403, 404], \
        f"Ожидался 400, 403 или 404, получен {response.status_code}"

    body = response.json()
    assert body.get("status") == "ERROR", "Статус должен быть ERROR"
    assert "errors" in body, "В ответе должны быть ошибки"

    validate(body, schema=shema_outlet_error)


@allure.feature("Outlets")
@allure.story("DELETE /campaigns/{campaignId}/outlets/{outletId} — без авторизации")
def test_delete_outlet_unauthorized(api_no_auth):
    """Негативный тест: Удаление точки выдачи без авторизации"""

    response = api_no_auth.delete(f'/campaigns/{CAMPAIGN_ID}/outlets/999999999')

    assert response.status_code in [401, 403], \
        f"Ожидался 401 или 403, получен {response.status_code}"

    body = response.json()
    assert body.get("status") == "ERROR"


@allure.feature("Outlets")
@allure.story("DELETE /campaigns/{campaignId}/outlets/{outletId} — неверный campaignId")
def test_delete_outlet_invalid_campaign(api):
    """Негативный тест: Удаление точки выдачи с несуществующим campaignId"""

    response = api.delete('/campaigns/999999999/outlets/999999999')

    assert response.status_code in [403, 404], \
        f"Ожидался 403 или 404, получен {response.status_code}"

    body = response.json()
    assert body.get("status") == "ERROR"
