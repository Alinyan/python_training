# -*- coding: utf-8 -*-
import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DBFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_list_groups(self):
        list_group = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor.fetchall():
                (id, name, header, footer) = row
                list_group.append(Group(id=str(id), name=str(name), header=str(header), footer=str(footer)))
        finally:
            cursor.close()
        return list_group

    def get_list_contacts(self):
        list_contact = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, middlename, lastname, nickname, company, title, address, home, "
                           "mobile, work, fax, email, email2, email3, homepage, address2, phone2, notes FROM addressbook where deprecated is null")
            for row in cursor.fetchall():
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax,
                 email, email2, email3, homepage, address2, phone2, notes) = row
                list_contact.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                    nickname=nickname, title=title, company=company, address1=address, home_phone=home,
                                    mobile_phone=mobile, work_phone=work, fax=fax, email=email, email2=email2,
                                    email3=email3, homepage=homepage, address2=address2, phone2=phone2, notes=notes))
        finally:
            cursor.close()
        return list_contact

    def destroy(self):
        self.connection.close()


