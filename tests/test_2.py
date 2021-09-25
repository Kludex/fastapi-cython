from typing import Optional

import httpx
import pytest

PREFIX = "/case-2"


@pytest.mark.parametrize(
    "params",
    [
        {"int_optional": 1, "str_optional": "hi"},
        {"str_optional": "hi"},
        {"int_optional": 1},
    ],
)
@pytest.mark.asyncio
async def test_get_model(client: httpx.AsyncClient, params: dict):
    res = await client.get(f"{PREFIX}/1", params=params)
    assert res.status_code == 200, res.json()
    assert res.json() == dict(integer=1, string="string", **params), res.json()
