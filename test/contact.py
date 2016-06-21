# -*- coding: utf-8 -*-
from model.contact import Contact
from data.contact import constant_data as testdata
import random
import pytest


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_list_contacts = app.contact.get_list_contacts()
    app.contact.create(contact)
    assert len(old_list_contacts) + 1 == app.contact.count()
    new_list_contacts = app.contact.get_list_contacts()
    old_list_contacts.append(contact)
    assert sorted(new_list_contacts, key=Contact.id) == sorted(old_list_contacts, key=Contact.id)

def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Olga", middlename="Petrovna", lastname="Petrova", nickname="Star", title="economist", company="OAO Dream-House",
                        address1="Russia, Lenina 5", home_phone="7894563", mobile_phone="9221547586", work_phone="6123457", fax="6123458",
                        email2="olga-star@oao-dream-house.com", email3="olga@dh.com", homepage="www.dream-house.com", address2="Russia, Spb, Lenina 17", phone2="145", notes="Likes to read books"))
    old_list_contacts = app.contact.get_list_contacts()
    index = random.randrange(len(old_list_contacts))
    app.contact.delete_random_contact(index)
    assert len(old_list_contacts) - 1 == app.contact.count()
    new_list_contacts = app.contact.get_list_contacts()
    old_list_contacts[index:index+1] = []
    assert old_list_contacts == new_list_contacts

def test_edit_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Olga", middlename="Petrovna", lastname="Petrova", nickname="Star", title="economist", company="OAO Dream-House",
                        address1="Russia, Lenina 5", home_phone="7894563", mobile_phone="9221547586", work_phone="6123457", fax="6123458",
                        email2="olga-star@oao-dream-house.com", email3="olga@dh.com", homepage="www.dream-house.com", address2="Russia, Spb, Lenina 17", phone2="145", notes="Likes to read books"))
    old_list_contacts = app.contact.get_list_contacts()
    contact = Contact(firstname="Marina", middlename="Ivanovna", lastname="Ivanova", nickname="PrettyGirl", title="economist", company="OAO Dream-House",
                        address1="Russia, Lenina 10", home_phone="8889652", mobile_phone="9261234567", work_phone="3654578", fax="9871245", email="mar@mail.ru",
                        email2="marina@oao-dream-house.com", email3="marina_cool@dh.com", homepage="www.dream-house.com", address2="Russia, Spb, Lenina 17", phone2="145", notes="Likes to swim")
    index = random.randrange(len(old_list_contacts))
    contact.id = old_list_contacts[index].id
    app.contact.edit_random_contact(index, contact)
    assert len(old_list_contacts) == app.contact.count()
    new_list_contacts = app.contact.get_list_contacts()
    old_list_contacts[index] = contact
    assert sorted(new_list_contacts, key=Contact.id) == sorted(old_list_contacts, key=Contact.id)

def test_contact_on_edit_page(app):
    contacts = app.contact.get_list_contacts()
    index = random.randrange(len(contacts))
    contact_from_home_page = app.contact.get_list_contacts()[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address1 == contact_from_edit_page.address1
    assert contact_from_home_page.emails_from_home_page == app.contact.merge_emails(contact_from_edit_page)
    assert contact_from_home_page.phones_from_home_page == app.contact.merge_phones(contact_from_edit_page)

# def test_contact_on_view_page(app):
#     contacts = app.contact.get_list_contacts()
#     index = random.randrange(len(contacts))
#     contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
#     contact_from_view_page = app.contact.get_contact_from_view_page(index)
#     assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
#     assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
#     assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
#     assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


