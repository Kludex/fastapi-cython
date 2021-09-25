import httpx
import pytest

PREFIX = "/case-1"


@pytest.mark.asyncio
async def test_get_model(client: httpx.AsyncClient):
    res = await client.get(f"{PREFIX}/1")
    assert res.status_code == 200
    assert res.json() == {"integer": 1, "string": "string"}
