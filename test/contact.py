# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_add_contact(app, db, check_ui, json_contacts):
    if len(db.get_list_contacts()) == 0:
        app.contact.create(json_contacts)
    old_list_contacts = db.get_list_contacts()
    app.contact.create(json_contacts)
    new_list_contacts = db.get_list_contacts()
    old_list_contacts.append(json_contacts)
    assert sorted(new_list_contacts, key=Contact.id_or_max) == sorted(old_list_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_list_contacts, key=Contact.id_or_max) == sorted(app.contact.get_list_contacts(), key=Contact.id_or_max)

def test_delete_random_contact(app, db, check_ui, data_contacts):
    if len(db.get_list_contacts()) == 0:
        app.contact.create(data_contacts)
    old_list_contacts = db.get_list_contacts()
    contact = random.choice(old_list_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_list_contacts = db.get_list_contacts()
    old_list_contacts.remove(contact)
    assert old_list_contacts == new_list_contacts
    if check_ui:
        assert sorted(new_list_contacts, key=Contact.id_or_max) == sorted(app.contact.get_list_contacts(), key=Contact.id_or_max)

def test_edit_random_contact(app, db, check_ui, data_contacts):
    if len(db.get_list_contacts()) == 0:
        app.contact.create(data_contacts)
    old_list_contacts = db.get_list_contacts()
    random_contact = random.choice(old_list_contacts)
    index = old_list_contacts.index(random_contact)
    edit_contact = Contact(firstname="Marina", middlename="Ivanovna", lastname="Ivanova", nickname="PrettyGirl",
                           title="economist", company="OAO Dream-House", address1="Russia, Lenina 10",
                           home_phone="8889652", mobile_phone="9261234567", work_phone="3654578", fax="9871245",
                           email="mar@mail.ru", email2="marina@oao-dream-house.com", email3="marina_cool@dh.com",
                           homepage="www.dream-house.com", address2="Russia, Spb, Lenina 17", phone2="145", notes="Likes to swim")
    edit_contact.id = random_contact.id
    app.contact.edit_contact_by_id(edit_contact)
    assert len(old_list_contacts) == app.contact.count()
    new_list_contacts = db.get_list_contacts()
    old_list_contacts[index] = edit_contact
    assert sorted(new_list_contacts, key=Contact.id_or_max) == sorted(old_list_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_list_contacts, key=Contact.id_or_max) == sorted(app.contact.get_list_contacts(), key=Contact.id_or_max)

def test_contact_on_edit_page(app):
    contacts = app.contact.get_list_contacts()
    index = random.randrange(len(contacts))
    contact_from_home_page = app.contact.get_list_contacts()[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address1 == contact_from_edit_page.address1
    assert contact_from_home_page.all_emails == app.contact.merge_emails(contact_from_edit_page)
    assert contact_from_home_page.all_phones == app.contact.merge_phones(contact_from_edit_page)
