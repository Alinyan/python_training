import pytest
import os.path
import json
from fixture.application import Application

fixture = None
conf = None

@pytest.fixture
def app(request):
    global fixture
    global conf
    browser = request.config.getoption("--browser")
    if conf is None:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--config"))) as json_file:
            config = json.load(json_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, baseURL=config["baseURL"])
    fixture.session.ensure_login(username=config["username"], password=config["password"])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def exit():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(exit)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--config", action="store", default="config.json")



