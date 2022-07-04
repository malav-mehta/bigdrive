from urllib.parse import urljoin

import requests

from .error import exit_if_error
from .metadata import get_config
from ..auth import firebase

HOST = "http://localhost:8080/"
API_VERSION = 1
API_PREFIX = f"api/v{API_VERSION}/"

BASE_URL = urljoin(HOST, API_PREFIX)


def _get_url(endpoint: str) -> str:
    return urljoin(BASE_URL, endpoint)


def _headers_with_auth(base_headers: dict | None = None) -> dict:
    if base_headers is None:
        base_headers = {}

    base_headers["Authorization"] = "Bearer {}".format(get_config()["id_token"])
    return base_headers


def _check_token_expired(result: dict) -> bool:
    return "error" in result and result["error"]["message"] == "TOKEN_EXPIRED"


def get(endpoint: str) -> dict | list:
    result = requests.get(_get_url(endpoint), headers=_headers_with_auth()).json()

    if _check_token_expired(result):
        firebase.auth.refresh_token()
        result = requests.get(_get_url(endpoint), headers=_headers_with_auth()).json()
    exit_if_error(result)

    return result


def post(endpoint: str, data: dict | None = None) -> dict | list:
    result = requests.post(_get_url(endpoint), data=data, headers=_headers_with_auth()).json()

    if _check_token_expired(result):
        firebase.auth.refresh_token()
        result = requests.post(_get_url(endpoint), data=data, headers=_headers_with_auth()).json()
    exit_if_error(result)

    return result
