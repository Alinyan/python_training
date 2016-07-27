
from pytest_bdd import given, when, then
from model.contact import Contact
import random

@given('a contact list')
def contact_list(db):
    return db.get_list_contacts()

@given('a contact with <firstname>, <lastname>, <middlename>, <nickname>, <title>, <company>, <address>, <email2>, <email3>, <work_phone>, <home_phone>, <mobile_phone>, <fax>, <homepage>, <address2>, <phone2> and <notes>')
def new_contact(firstname, lastname, middlename, nickname, title, company, address, email2, email3, work_phone, home_phone, mobile_phone, fax, homepage, address2, phone2, notes):
    return Contact(firstname=firstname, lastname=lastname, middlename=middlename, nickname=nickname, title=title, company=company,
                   address1=address, email2=email2, email3=email3, home_phone=home_phone, work_phone=work_phone,
                   mobile_phone=mobile_phone, fax=fax, homepage=homepage, address2=address2, phone2=phone2, notes=notes)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)

@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_list_contacts()
    old_contacts.append(new_contact)
    assert len(old_contacts) == len(db.get_list_contacts())
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_list_contacts()) == 0:
        app.contact.create(Contact(firstname="Marina", middlename="Ivanovna", lastname="Ivanova", nickname="PrettyGirl",
                           title="economist", company="OAO Dream-House", address1="Russia, Lenina 10",
                           home_phone="8889652", mobile_phone="9261234567", work_phone="3654578", fax="9871245",
                           email="mar@mail.ru", email2="marina@oao-dream-house.com", email3="marina_cool@dh.com",
                           homepage="www.dream-house.com", address2="Russia, Spb, Lenina 17", phone2="145", notes="Likes to swim"))
    return db.get_list_contacts()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then('the new contact list is equal to the old contact list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_list_contacts()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_list_contacts(), key=Contact.id_or_max)

@given('a index of the edited contact')
def index_contact(non_empty_contact_list, random_contact):
    return non_empty_contact_list.index(random_contact)

@when('I edit the contact from the list')
def edit_contact(app, new_contact, random_contact):
    new_contact.id = random_contact.id
    app.contact.edit_contact_by_id(new_contact)

@then('the new contact list is equal to the old contact list with edited contact')
def verify_contact_edited(db, non_empty_contact_list, new_contact, index_contact, app, check_ui):
    old_lists = non_empty_contact_list
    new_lists = db.get_list_contacts()
    old_lists[index_contact] = new_contact
    assert sorted(new_lists, key=Contact.id_or_max) == sorted(old_lists, key=Contact.id_or_max)
    if check_ui:
        app.contact.check_ui_data(new_lists)





