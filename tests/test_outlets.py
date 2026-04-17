import allure
from jsonschema import validate

import config
from schemas.schema_outlets import schema_outlet_error

pytestmark = [allure.feature("Outlets")]


@allure.title("Удаление несуществующей точки выдачи — 400/403/404")
def test_delete_outlet_not_found(api):
    response = api.delete(f'/campaigns/{config.campaign_id}/outlets/999999999')

    assert response.status_code in [400, 403, 404]

    body = response.json()
    assert body.get("status") == "ERROR"
    assert "errors" in body

    validate(body, schema=schema_outlet_error)


@allure.title("Удаление точки выдачи без авторизации — 401/403")
def test_delete_outlet_unauthorized(api_no_auth):
    response = api_no_auth.delete(f'/campaigns/{config.campaign_id}/outlets/999999999')

    assert response.status_code in [401, 403]
    assert response.json().get("status") == "ERROR"


@allure.title("Удаление точки выдачи с несуществующим campaignId — 403/404")
def test_delete_outlet_invalid_campaign(api):
    response = api.delete('/campaigns/999999999/outlets/999999999')

    assert response.status_code in [403, 404]
    assert response.json().get("status") == "ERROR"

