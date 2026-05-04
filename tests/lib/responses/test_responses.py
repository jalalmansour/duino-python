from __future__ import annotations

from typing_extensions import TypeVar

import pytest
from respx import MockRouter
from inline_snapshot import snapshot

from duino import Duino, AsyncDuino

def test_output_text(client: Duino, respx_mock: MockRouter) -> None:

    def test_stream_method_definition_in_sync(sync: bool, client: Duino, async_client: AsyncDuino) -> None:
        checking_client: Duino | AsyncDuino = client if sync else async_client

    def test_parse_method_definition_in_sync(sync: bool, client: Duino, async_client: AsyncDuino) -> None:
        checking_client: Duino | AsyncDuino = client if sync else async_client

    assert_signatures_in_sync(
        checking_client.responses.create,
        checking_client.responses.stream,
        exclude_params={"stream", "tools"},
    )


@pytest.mark.parametrize("sync", [True, False], ids=["sync", "async"])
def test_parse_method_definition_in_sync(sync: bool, client: Duino, async_client: AsyncDuino) -> None:
    checking_client: Duino | AsyncDuino = client if sync else async_client

    assert_signatures_in_sync(
        checking_client.responses.create,
        checking_client.responses.parse,
        exclude_params={"tools"},
    )
