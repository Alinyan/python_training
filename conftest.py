import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def exit():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(exit)
    return fixture


