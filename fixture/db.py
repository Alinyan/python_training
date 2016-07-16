# -*- coding: utf-8 -*-
import pymysql.cursors
from model.group import Group

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
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor.fetchall():
                (id, name, header, footer) = row
                list_contact.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list_contact

    def destroy(self):
        self.connection.close()


