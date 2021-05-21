import betteraiohttp
import asyncio
import pytest


@pytest.fixture
def url():
    return 'rick.bobdotcom.xyz'


@pytest.fixture
def session():
    """Returns a session"""
    return betteraiohttp.ClientSession()


@pytest.mark.asyncio
async def test_conversions(session, url):
    assert (await session.get(url)).rickroll
