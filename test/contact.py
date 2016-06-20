# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import pytest
import string

def random_string(prefix, maxlen):
    char = string.ascii_letters + string.hexdigits + string.punctuation + ' '*15
    return prefix + "".join([random.choice(char) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=fn, middlename=mn, lastname=ln, nickname=nn, title=t, company=c, address1=a1, home_phone=hp,
            mobile_phone=mp, work_phone=wp, fax=f, email2=e2, email3=e3, homepage=h, address2=a2, phone2=p2, notes=n)
    for fn in ["", random_string("Firstname", 20)]
    for mn in ["", random_string("Middlename", 20)]
    for ln in ["", random_string("Lastname", 20)]
    for nn in ["", random_string("Nickname", 20)]
    for t in ["", random_string("title", 20)]
    for c in ["", random_string("company", 20)]
    for a1 in ["", random_string("address1", 50)]
    for hp in ["", random_string("homephone", 15)]
    for mp in ["", random_string("mobilephone", 15)]
    for wp in ["", random_string("workphone", 15)]
    for f in ["", random_string("fax", 15)]
    for e2 in ["", random_string("email2", 30)]
    for e3 in ["", random_string("email3", 30)]
    for h in ["", random_string("homepage", 30)]
    for a2 in ["", random_string("address2", 50)]
    for p2 in ["", random_string("phone2", 15)]
    for n in ["", random_string("notes", 100)]
]

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

def test_contact_on_view_page(app):
    contacts = app.contact.get_list_contacts()
    index = random.randrange(len(contacts))
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


