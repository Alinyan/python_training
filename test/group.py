# -*- coding: utf-8 -*-
from model.group import Group
import random
import re


def test_add_group(app, db, check_ui, json_groups):
    old_list_groups = db.get_list_groups()
    app.group.create(json_groups)
    new_list_groups = db.get_list_groups()
    old_list_groups.append(json_groups)
    assert sorted(new_list_groups, key=Group.id_or_max) == sorted(old_list_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_list_groups, key=Group.id_or_max) == sorted(app.group.get_list_groups(), key=Group.id_or_max)

def test_delete_group_by_id(app, db, check_ui, data_groups):
    if len(db.get_list_groups()) == 0:
        app.group.create(data_groups)
    old_list_groups = db.get_list_groups()
    group = random.choice(old_list_groups)
    app.group.delete_group_by_id(group.id)
    new_list_groups = db.get_list_groups()
    old_list_groups.remove(group)
    assert old_list_groups == new_list_groups
    if check_ui:
        assert sorted(new_list_groups, key=Group.id_or_max) == sorted(app.group.get_list_groups(), key=Group.id_or_max)

def test_edit_first_group(app, db, check_ui, data_groups):
    if len(db.get_list_groups()) == 0:
        app.group.create(data_groups)
    old_list_groups = db.get_list_groups()
    edit_group = Group(name="Name_of_group_new", header="Header_of_group_new", footer="Footer_of_group_new")
    edit_group.id = old_list_groups[0].id
    app.group.edit_group_by_id(edit_group)
    new_list_groups = db.get_list_groups()
    old_list_groups[0] = edit_group
    assert sorted(new_list_groups, key=Group.id_or_max) == sorted(old_list_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_list_groups, key=Group.id_or_max) == sorted(app.group.get_list_groups(), key=Group.id_or_max)

def test_modify_group_name(app, db, check_ui, data_groups):
    if len(db.get_list_groups()) == 0:
        app.group.create(data_groups)
    old_list_groups = db.get_list_groups()
    random_group = random.choice(old_list_groups)
    index = old_list_groups.index(random_group)
    edit_group = Group(name="New group 1324")
    edit_group.id = random_group.id
    app.group.edit_group_by_id(edit_group)
    new_list_groups = db.get_list_groups()
    old_list_groups[index] = edit_group
    assert sorted(new_list_groups, key=Group.id_or_max) == sorted(old_list_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_list_groups, key=Group.id_or_max) == sorted(app.group.get_list_groups(), key=Group.id_or_max)

def test_modify_group_header(app, db, check_ui, data_groups):
    if len(db.get_list_groups()) == 0:
        app.group.create(data_groups)
    old_list_groups = db.get_list_groups()
    random_group = random.choice(old_list_groups)
    index = old_list_groups.index(random_group)
    edit_group = Group(header="New header 125484")
    edit_group.id = random_group.id
    app.group.edit_group_by_id(edit_group)
    new_list_groups = db.get_list_groups()
    old_list_groups[index] = edit_group
    assert sorted(new_list_groups, key=Group.id_or_max) == sorted(old_list_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_list_groups, key=Group.id_or_max) == sorted(app.group.get_list_groups(), key=Group.id_or_max)

def test_group_list(app, db):
    def clean(group):
        return Group(id=group.id, name=re.sub(r'\s+', ' ', group.name.strip()))
    sorted_db_list = sorted(map(clean, db.get_list_groups()), key=Group.id_or_max)
    sorted_ui_list = sorted(app.group.get_list_groups(), key=Group.id_or_max)
    assert sorted_ui_list == sorted_db_list