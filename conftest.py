import pytest
import config
from api_client import APIClient


@pytest.fixture(scope='session')
def api():
    return APIClient(
        config.base_url,
        {"Api-Key": config.api_key, "Content-Type": "application/json"}
    )


@pytest.fixture(scope='session')
def api_no_auth():
    return APIClient(
        config.base_url,
        {"Content-Type": "application/json"}
    )


@pytest.fixture(scope='session')
def api_invalid_auth():
    return APIClient(
        config.base_url,
        {"Api-Key": "INVALID_TOKEN_12345", "Content-Type": "application/json"}
    )
