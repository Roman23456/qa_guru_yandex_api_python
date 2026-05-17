import logging
import allure
import requests

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
        url = self.base_url + endpoint
        logger.info(f"GET | {url} | params: {kwargs.get('params')}")
        with allure.step(f"GET {endpoint}"):
            response = self.session.get(url, **kwargs)
            logger.info(f"GET | {response.status_code} | {response.url}")
            self._attach_to_allure(response)
        return response

    def post(self, endpoint: str, **kwargs):
        url = self.base_url + endpoint
        logger.info(f"POST | {url} | body: {kwargs.get('json')}")
        with allure.step(f"POST {endpoint}"):
            response = self.session.post(url, **kwargs)
            logger.info(f"POST | {response.status_code} | {response.url}")
            self._attach_to_allure(response)
        return response

    def delete(self, endpoint: str, **kwargs):
        url = self.base_url + endpoint
        logger.info(f"DELETE | {url}")
        with allure.step(f"DELETE {endpoint}"):
            response = self.session.delete(url, **kwargs)
            logger.info(f"DELETE | {response.status_code} | {response.url}")
            self._attach_to_allure(response)
        return response
