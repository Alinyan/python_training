import pytest
import os.path
import json
from fixture.application import Application
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

class Addressbook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="config.json", browser="chrome"):
        self.browser = browser
        conf = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(conf) as f:
            self.config = json.load(f)

    def init_fixtures(self):
        web_config = self.config['web']
        self.fixture = Application(browser=self.browser, baseURL=web_config["baseURL"])
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.config['db']
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
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def edit_group(self, random_group, edit_group):
        edit_group.id = random_group.id
        self.fixture.group.edit_group_by_id(edit_group)

    def replace_values_list(self, old_list, index, edit_value):
        old_list[index] = edit_value

    def get_contact_list(self):
        return self.dbfixture.get_list_contacts()

    def new_contact(self, firstname=None, lastname=None, middlename=None, nickname=None, title=None, company=None,
                    address=None, email2=None, email3=None, work_phone=None, mobile_phone=None, home_phone=None, fax=None,
                    homepage=None, notes=None, phone2=None, address2=None):
        return Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
                       company=company, address1=address, home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, fax=fax, email2=email2, email3=email3, homepage=homepage,
                       address2=address2, phone2=phone2, notes=notes)

    def create_contact(self, contact):
        self.fixture.contact.create(contact)

    def contact_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)

    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id)

    def edit_contact(self, random_contact, edit_contact):
        edit_contact.id = random_contact.id
        self.fixture.contact.edit_contact_by_id(edit_contact)