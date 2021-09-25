import asyncio

import httpx
import pytest
from app.main import app


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    """Reference: https://github.com/pytest-dev/pytest-asyncio/issues/38#issuecomment-264418154"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(name="client", scope="session")
async def httpx_client():
    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        yield client
