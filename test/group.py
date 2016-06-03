# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

def test_delete_first_group(app):
    app.group.delete_first_group()

def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="Name_of_group_new", header="Header_of_group_new", footer="Footer_of_group_new"))

def test_modify_group_name(app):
    app.group.edit_first_group(Group(name="New group 1111111111"))

def test_modify_group_header(app):
    app.group.edit_first_group(Group(header="New header 2222222"))


