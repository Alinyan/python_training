# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import re

def test_add_contact(app, json_contacts):
    old_list_contacts = app.contact.get_list_contacts()
    app.contact.create(json_contacts)
    assert len(old_list_contacts) + 1 == app.contact.count()
    new_list_contacts = app.contact.get_list_contacts()
    old_list_contacts.append(json_contacts)
    assert sorted(new_list_contacts, key=Contact.id) == sorted(old_list_contacts, key=Contact.id)

def test_delete_random_contact(app, data_contacts):
    if app.contact.count() == 0:
        app.contact.create(data_contacts)
    old_list_contacts = app.contact.get_list_contacts()
    index = random.randrange(len(old_list_contacts))
    app.contact.delete_random_contact(index)
    assert len(old_list_contacts) - 1 == app.contact.count()
    new_list_contacts = app.contact.get_list_contacts()
    old_list_contacts[index:index+1] = []
    assert old_list_contacts == new_list_contacts

def test_edit_random_contact(app, data_contacts):
    if app.contact.count() == 0:
        app.contact.create(data_contacts)
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

def test_contact_list(app, db):
    def clean(contact):
        return Contact(id=contact.id, name=re.sub(r'\s+', ' ', contact.name.strip()))
    sorted_db_list = sorted(map(clean, db.get_list_contacts()), key=Contact.id_or_max)
    sorted_ui_list = sorted(app.contact.get_list_contacts(), key=Contact.id_or_max)
    assert sorted_ui_list == sorted_db_list

# def test_contact_on_view_page(app):
#     contacts = app.contact.get_list_contacts()
#     index = random.randrange(len(contacts))
#     contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
#     contact_from_view_page = app.contact.get_contact_from_view_page(index)
#     assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
#     assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
#     assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
#     assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


