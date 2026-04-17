import logging
import allure
import pytest
import requests
import config


logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s | %(asctime)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, base_url: str, headers: dict):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(headers)

    def _request(self, method: str, endpoint: str, **kwargs):
        url = self.base_url + endpoint
        response = self.session.request(method, url, **kwargs)
        logger.info(f"{method.upper()} | {response.status_code} | {response.url}")
        self._attach_to_allure(response)
        return response

    @staticmethod
    def _attach_to_allure(response: requests.Response):
        request_body = response.request.body
        if isinstance(request_body, bytes):
            request_body = request_body.decode('utf-8')
        allure.attach(
            body=request_body or '',
            name="Request body",
            attachment_type=allure.attachment_type.JSON
        )
        allure.attach(
            body=response.text,
            name="Response body",
            attachment_type=allure.attachment_type.JSON
        )

    def get(self, endpoint: str, **kwargs):
        return self._request('GET', endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request('POST', endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request('DELETE', endpoint, **kwargs)


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

