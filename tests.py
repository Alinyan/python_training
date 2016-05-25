# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from group import Group
from user import User


@pytest.fixture
def user(request):
    fixture = User()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(user):
    user.login(username="admin", password="secret")
    user.create_group(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
    user.logout()

def test_add_empty_group(user):
    user.login(username="admin", password="secret")
    user.create_group(Group(name="", header="", footer=""))
    user.logout()

def test_add_contact(user):
    user.login(username="admin", password="secret")
    user.create_contact(Contact(firstname="Olga", middlename="Petrovna", lastname="Petrova", nickname="Star", title="economist", company="OAO Dream-House",
                        address_company="Russia, Lenina 5", home_phone="7894563", mobile_phone="9221547586", work_phone="6123457", fax="6123458",
                        email2="olga-star@oao-dream-house.com", email3="olga@dh.com", homepage="www.dream-house.com", address2="Russia, Spb, Lenina 17", phone2="145", notes="Likes to read books"))
    user.logout()

def test_add_empty_contact(user):
    user.login(username="admin", password="secret")
    user.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                        address_company="", home_phone="", mobile_phone="", work_phone="", fax="",
                        email2="", email3="", homepage="", address2="", phone2="", notes=""))
    user.logout()
