import httpx
import pytest

PREFIX = "/case-3"


@pytest.mark.parametrize("value,expected", [(1, 200), (-1, 422)])
@pytest.mark.asyncio
async def test_get_model(client: httpx.AsyncClient, value: str, expected: int):
    res = await client.get(f"{PREFIX}/{value}")
    assert res.status_code == expected
