# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_add_group(app, json_groups):
    old_list_groups = app.group.get_list_groups()
    app.group.create(json_groups)
    assert len(old_list_groups) + 1 == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups.append(json_groups)
    assert sorted(new_list_groups, key=Group.id) == sorted(old_list_groups, key=Group.id)

def test_delete_random_group(app, data_groups):
    if app.group.count() == 0:
        app.group.create(data_groups)
    old_list_groups = app.group.get_list_groups()
    index = random.randrange(len(old_list_groups))
    app.group.delete_random_group(index)
    assert len(old_list_groups) - 1 == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups[index:index+1] = []
    assert old_list_groups == new_list_groups

def test_edit_first_group(app, data_groups):
    if app.group.count() == 0:
        app.group.create(data_groups)
    old_list_groups = app.group.get_list_groups()
    group = Group(name="Name_of_group_new", header="Header_of_group_new", footer="Footer_of_group_new")
    group.id = old_list_groups[0].id
    app.group.edit_first_group(group)
    assert len(old_list_groups) == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups[0] = group
    assert sorted(new_list_groups, key=Group.id) == sorted(old_list_groups, key=Group.id)

def test_modify_group_name(app, data_groups):
    if app.group.count() == 0:
        app.group.create(data_groups)
    old_list_groups = app.group.get_list_groups()
    group = Group(name="New group 1111111324")
    index = random.randrange(len(old_list_groups))
    group.id = old_list_groups[index].id
    app.group.edit_random_group(index, group)
    assert len(old_list_groups) == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups[index] = group
    assert sorted(new_list_groups, key=Group.id) == sorted(old_list_groups, key=Group.id)

def test_modify_group_header(app, data_groups):
    if app.group.count() == 0:
        app.group.create(data_groups)
    old_list_groups = app.group.get_list_groups()
    group = Group(header="Header_of_group_new")
    index = random.randrange(len(old_list_groups))
    group.id = old_list_groups[index].id
    app.group.edit_random_group(index, group)
    assert len(old_list_groups) == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups[index] = group
    assert sorted(new_list_groups, key=Group.id) == sorted(old_list_groups, key=Group.id)
