import allure
from jsonschema import validate

import config
from schemas.schema_outlets import schema_outlet_error

pytestmark = [allure.feature("Outlets")]


@allure.title("Удаление несуществующей точки выдачи")
def test_delete_outlet_not_found(api):
    response = api.delete(f'/campaigns/{config.campaign_id}/outlets/999999999')

    assert response.status_code == 400

    body = response.json()
    assert body.get("status") == "ERROR"
    assert "errors" in body

    validate(body, schema=schema_outlet_error)


@allure.title("Удаление точки выдачи без авторизации")
def test_delete_outlet_unauthorized(api_no_auth):
    response = api_no_auth.delete(f'/campaigns/{config.campaign_id}/outlets/999999999')

    assert response.status_code == 401
    assert response.json().get("status") == "ERROR"


@allure.title("Удаление точки выдачи с несуществующим campaignId")
def test_delete_outlet_invalid_campaign(api):
    response = api.delete('/campaigns/999999999/outlets/999999999')

    assert response.status_code == 403
    assert response.json().get("status") == "ERROR"

