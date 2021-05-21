import betteraiohttp


tests = ['rick.bobdotcom.xyz']


@pytest.fixture
def session():
    """Returns a session"""
    return betteraiohttp.ClientSession()


@pytest.mark.parametrize("url", tests)
def test_conversions(session, url):
    assert session.get(url).rickroll
