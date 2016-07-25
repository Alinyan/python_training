import pytest
import os.path
import json
import importlib
import jsonpickle
from fixture.application import Application
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

class Addressbook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        conf = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with conf as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, baseURL=web_config["baseURL"])
        self.fixture.session.ensure_login(username=web_conf["username"], password=web_conf["password"])
        db_config = self.target['db']
        self.dbfixture = ORMFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])

    def destroy_fixtures(self):
        #self.dbfixture.destroy
        self.fixture.destroy()

    def create_group(self, name, header, footer):
        self.fixture.group.create(Group(name=name, header=header, footer=footer))