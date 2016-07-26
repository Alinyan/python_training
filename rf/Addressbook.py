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
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.target['db']
        self.dbfixture = ORMFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])

    def destroy_fixtures(self):
        #self.dbfixture.destroy
        self.fixture.destroy()

    def create_group(self, group):
        self.fixture.group.create(group)

    def get_group_list(self):
        return self.dbfixture.get_list_groups()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)
