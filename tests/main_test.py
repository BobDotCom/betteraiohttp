import betteraiohttp
import asyncio


tests = ['rick.bobdotcom.xyz']


@pytest.fixture
def session():
    """Returns a session"""
    return betteraiohttp.ClientSession()


@pytest.mark.parametrize("url", tests)
def test_conversions(session, url):
    assert asyncio.run(session.get(url)).rickroll
