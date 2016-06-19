# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_list_groups = app.group.get_list_groups()
    group = Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group")
    app.group.create(group)
    assert len(old_list_groups) + 1 == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups.append(group)
    assert sorted(new_list_groups, key=Group.id) == sorted(old_list_groups, key=Group.id)

def test_add_empty_group(app):
    old_list_groups = app.group.get_list_groups()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    assert len(old_list_groups) + 1 == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups.append(group)
    assert sorted(new_list_groups, key=Group.id) == sorted(old_list_groups, key=Group.id)

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
    old_list_groups = app.group.get_list_groups()
    app.group.delete_first_group()
    assert len(old_list_groups) - 1 == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups[0:1] = []
    assert old_list_groups == new_list_groups

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
    old_list_groups = app.group.get_list_groups()
    group = Group(name="Name_of_group_new", header="Header_of_group_new", footer="Footer_of_group_new")
    group.id = old_list_groups[0].id
    app.group.edit_first_group(group)
    assert len(old_list_groups) == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups[0] = group
    assert sorted(new_list_groups, key=Group.id) == sorted(old_list_groups, key=Group.id)

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
    old_list_groups = app.group.get_list_groups()
    group = Group(name="New group 1111111324")
    group.id = old_list_groups[0].id
    app.group.edit_first_group(group)
    assert len(old_list_groups) == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups[0] = group
    assert sorted(new_list_groups, key=Group.id) == sorted(old_list_groups, key=Group.id)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
    old_list_groups = app.group.get_list_groups()
    group = Group(header="Header_of_group_new")
    group.id = old_list_groups[0].id
    app.group.edit_first_group(group)
    assert len(old_list_groups) == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups[0] = group
    assert sorted(new_list_groups, key=Group.id) == sorted(old_list_groups, key=Group.id)
