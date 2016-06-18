# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_list_groups = app.group.get_count_groups()
    app.group.create(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
    new_list_groups = app.group.get_count_groups()
    assert len(old_list_groups) + 1 == len(new_list_groups)

def test_add_empty_group(app):
    old_list_groups = app.group.get_count_groups()
    app.group.create(Group(name="", header="", footer=""))
    new_list_groups = app.group.get_count_groups()
    assert len(old_list_groups) + 1 == len(new_list_groups)

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
    old_list_groups = app.group.get_count_groups()
    app.group.delete_first_group()
    new_list_groups = app.group.get_count_groups()
    assert len(old_list_groups) - 1 == len(new_list_groups)
    old_list_groups[0:1] = []
    assert old_list_groups == new_list_groups


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
    old_list_groups = app.group.get_count_groups()
    app.group.edit_first_group(Group(name="Name_of_group_new", header="Header_of_group_new", footer="Footer_of_group_new"))
    new_list_groups = app.group.get_count_groups()
    assert len(old_list_groups) == len(new_list_groups)

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
    old_list_groups = app.group.get_count_groups()
    app.group.edit_first_group(Group(name="New group 1111111111"))
    new_list_groups = app.group.get_count_groups()
    assert len(old_list_groups) == len(new_list_groups)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
    old_list_groups = app.group.get_count_groups()
    app.group.edit_first_group(Group(header="New header 2222222"))
    new_list_groups = app.group.get_count_groups()
    assert len(old_list_groups) == len(new_list_groups)


