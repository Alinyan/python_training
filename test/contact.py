# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import re

def test_add_contact1(app, db, check_ui, json_contacts):
    if len(db.get_list_contacts()) == 0:
        app.contact.create(json_contacts)
    old_list_contacts = db.get_list_contacts()
    app.contact.create(json_contacts)
    new_list_contacts = db.get_list_contacts()
    old_list_contacts.append(json_contacts)
    assert sorted(new_list_contacts, key=Contact.id_or_max) == sorted(old_list_contacts, key=Contact.id_or_max)
    if check_ui:
        app.contact.check_ui_data(new_list_contacts)

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
        app.contact.check_ui_data(new_list_contacts)

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
        app.contact.check_ui_data(new_list_contacts)

def test_contact_on_edit_page(app):
    contacts = app.contact.get_list_contacts()
    index = random.randrange(len(contacts))
    contact_from_home_page = app.contact.get_list_contacts()[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page.lastname == app.contact.make_one_space(contact_from_edit_page.lastname)
    assert contact_from_home_page.firstname == app.contact.make_one_space(contact_from_edit_page.firstname)
    assert contact_from_home_page.all_emails == app.contact.merge_emails(contact_from_edit_page)
    assert contact_from_home_page.all_phones == app.contact.merge_phones(contact_from_edit_page)

def test_add_contact_in_group(app, db, json_contacts, json_groups):
    if len(db.get_list_groups()) == 0:
        app.group.create(json_groups)
    group = random.choice(db.get_list_groups())
    old_list_contacts_with_group = db.get_contacts_in_group_by_name(group)
    app.contact.create_with_add_group(json_contacts, group.name)
    new_list_contacts_with_group = db.get_contacts_in_group_by_name(group)
    old_list_contacts_with_group.append(json_contacts)
    assert sorted(new_list_contacts_with_group, key=Contact.id_or_max) == sorted(old_list_contacts_with_group, key=Contact.id_or_max)

def test_delete_contact_from_group(app, db, json_contacts, json_groups):
    if len(db.get_list_groups()) == 0:
        app.group.create(json_groups)
    group = random.choice(db.get_list_groups())
    if len(db.get_contacts_in_group_by_name(group)) == 0:
        app.contact.create_with_add_group(json_contacts, group.name)
    contact = random.choice(db.get_contacts_in_group_by_name(group))
    old_list_contacts_with_group = db.get_contacts_in_group_by_name(group)
    old_list_contacts_without_group = db.get_contacts_not_in_group_by_name(group)
    app.contact.delete_contact_from_group(contact.id, group.name)
    new_list_contacts_with_group = db.get_contacts_in_group_by_name(group)
    new_list_contacts_without_group = db.get_contacts_not_in_group_by_name(group)
    old_list_contacts_with_group.remove(contact)
    old_list_contacts_without_group.append(contact)
    assert sorted(new_list_contacts_with_group, key=Contact.id_or_max) == sorted(old_list_contacts_with_group, key=Contact.id_or_max)
    assert sorted(new_list_contacts_without_group, key=Contact.id_or_max) == sorted(old_list_contacts_without_group, key=Contact.id_or_max)

def test_add_group_for_contact(app, db, json_contacts, json_groups):
    if len(db.get_list_groups()) == 0:
        app.group.create(json_groups)
    group = random.choice(db.get_list_groups())
    if len(db.get_contacts_not_in_group_by_name(group)) == 0:
        app.contact.create(json_contacts)
    contact = random.choice(db.get_contacts_not_in_group_by_name(group))
    old_list_contacts_with_group = db.get_contacts_in_group_by_name(group)
    app.contact.add_group(contact.id, group.name)
    new_list_contacts_with_group = db.get_contacts_in_group_by_name(group)
    old_list_contacts_with_group.append(contact)
    assert sorted(new_list_contacts_with_group, key=Contact.id_or_max) == sorted(old_list_contacts_with_group, key=Contact.id_or_max)

