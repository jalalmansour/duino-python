# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os as _os

import httpx
import pytest
from httpx import URL

import duino
from duino import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES


def reset_state() -> None:
    duino._reset_client()
    duino.api_key = None
    duino.admin_api_key = None
    duino.organization = None
    duino.project = None
    duino.webhook_secret = None
    duino.base_url = None
    duino.timeout = DEFAULT_TIMEOUT
    duino.max_retries = DEFAULT_MAX_RETRIES
    duino.default_headers = None
    duino.default_query = None
    duino.http_client = None
    duino.api_type = _os.environ.get("Duino_API_TYPE")  # type: ignore
    duino.api_version = None
    duino.azure_endpoint = None
    duino.azure_ad_token = None
    duino.azure_ad_token_provider = None


@pytest.fixture(autouse=True)
def reset_state_fixture() -> None:
    reset_state()


def test_base_url_option() -> None:
    assert duino.base_url is None
    assert duino.completions._client.base_url == URL("https://api.duino.com/v1/")

    duino.base_url = "http://foo.com"

    assert duino.base_url == URL("http://foo.com")
    assert duino.completions._client.base_url == URL("http://foo.com")


def test_timeout_option() -> None:
    assert duino.timeout == duino.DEFAULT_TIMEOUT
    assert duino.completions._client.timeout == duino.DEFAULT_TIMEOUT

    duino.timeout = 3

    assert duino.timeout == 3
    assert duino.completions._client.timeout == 3


def test_max_retries_option() -> None:
    assert duino.max_retries == duino.DEFAULT_MAX_RETRIES
    assert duino.completions._client.max_retries == duino.DEFAULT_MAX_RETRIES

    duino.max_retries = 1

    assert duino.max_retries == 1
    assert duino.completions._client.max_retries == 1


def test_default_headers_option() -> None:
    assert duino.default_headers == None

    duino.default_headers = {"Foo": "Bar"}

    assert duino.default_headers["Foo"] == "Bar"
    assert duino.completions._client.default_headers["Foo"] == "Bar"


def test_default_query_option() -> None:
    assert duino.default_query is None
    assert duino.completions._client._custom_query == {}

    duino.default_query = {"Foo": {"nested": 1}}

    assert duino.default_query["Foo"] == {"nested": 1}
    assert duino.completions._client._custom_query["Foo"] == {"nested": 1}


def test_http_client_option() -> None:
    assert duino.http_client is None

    original_http_client = duino.completions._client._client
    assert original_http_client is not None

    new_client = httpx.Client()
    duino.http_client = new_client

    assert duino.completions._client._client is new_client


import contextlib
from typing import Iterator

from duino.lib.azure import AzureDuino

        assert isinstance(client, AzureDuino)

        assert isinstance(client, AzureDuino)
        assert client._azure_ad_token == "example AD token"


def test_azure_azure_ad_token_provider_version_and_endpoint_env() -> None:
    with fresh_env():
        duino.api_type = None
        _os.environ["Duino_API_VERSION"] = "example-version"
        _os.environ["AZURE_Duino_ENDPOINT"] = "https://www.example"
        duino.azure_ad_token_provider = lambda: "token"

        client = duino.completions._client
        assert isinstance(client, AzureDuino)
        assert client._azure_ad_token_provider is not None
        assert client._azure_ad_token_provider() == "token"
