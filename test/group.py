# -*- coding: utf-8 -*-
from model.group import Group
import random
import re
import pytest


def test_add_group(app, db, check_ui, json_groups):
    with pytest.allure.step('Given a group list'):
        old_list_groups = db.get_list_groups()
    with pytest.allure.step('When I add a group %s to the list' % json_groups):
        app.group.create(json_groups)
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        new_list_groups = db.get_list_groups()
        old_list_groups.append(json_groups)
        assert sorted(new_list_groups, key=Group.id_or_max) == sorted(old_list_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_list_groups, key=Group.id_or_max) == sorted(app.group.get_list_groups(), key=Group.id_or_max)

def test_delete_group_by_id(app, db, check_ui, data_groups):
    with pytest.allure.step('Given a non-empty group list'):
        if len(db.get_list_groups()) == 0:
            app.group.create(data_groups)
        old_list_groups = db.get_list_groups()
    with pytest.allure.step('Given a random group from the list'):
        group = random.choice(old_list_groups)
    with pytest.allure.step('When I delete the group from the list'):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step('Then the new group list is equal to the old group list without the deleted group'):
        new_list_groups = db.get_list_groups()
        old_list_groups.remove(group)
        assert old_list_groups == new_list_groups
        if check_ui:
            assert sorted(new_list_groups, key=Group.id_or_max) == sorted(app.group.get_list_groups(), key=Group.id_or_max)

def test_edit_first_group(app, db, check_ui, data_groups):
    with pytest.allure.step('Given a non-empty group list'):
        if len(db.get_list_groups()) == 0:
            app.group.create(data_groups)
        old_list_groups = db.get_list_groups()
    edit_group = Group(name="Name_of_group_new", header="Header_of_group_new", footer="Footer_of_group_new")
    with pytest.allure.step('When I edit a first group from the list to edit group %s' % edit_group):
        edit_group.id = old_list_groups[0].id
        app.group.edit_group_by_id(edit_group)
    with pytest.allure.step('Then the new group list is equal to the old group list with edited group'):
        new_list_groups = db.get_list_groups()
        old_list_groups[0] = edit_group
        assert sorted(new_list_groups, key=Group.id_or_max) == sorted(old_list_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_list_groups, key=Group.id_or_max) == sorted(app.group.get_list_groups(), key=Group.id_or_max)

def test_modify_group_name(app, db, check_ui, data_groups):
    with pytest.allure.step('Given a non-empty group list'):
        if len(db.get_list_groups()) == 0:
            app.group.create(data_groups)
        old_list_groups = db.get_list_groups()
    with pytest.allure.step('Given a random group from the list'):
        random_group = random.choice(old_list_groups)
        index = old_list_groups.index(random_group)
        edit_group = Group(name="New group 1324")
    with pytest.allure.step('When I edit a group %s from the list to edit group %s' % (random_group, edit_group)):
        edit_group.id = random_group.id
        app.group.edit_group_by_id(edit_group)
    with pytest.allure.step('Then the new group list is equal to the old group list with edited group'):
        new_list_groups = db.get_list_groups()
        old_list_groups[index] = edit_group
        assert sorted(new_list_groups, key=Group.id_or_max) == sorted(old_list_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_list_groups, key=Group.id_or_max) == sorted(app.group.get_list_groups(), key=Group.id_or_max)

def test_modify_group_header(app, db, check_ui, data_groups):
    with pytest.allure.step('Given a non-empty group list'):
        if len(db.get_list_groups()) == 0:
            app.group.create(data_groups)
        old_list_groups = db.get_list_groups()
    with pytest.allure.step('Given a random group from the list'):
        random_group = random.choice(old_list_groups)
        index = old_list_groups.index(random_group)
        edit_group = Group(header="New header 125484")
    with pytest.allure.step('When I edit a group %s from the list to edit group %s' % (random_group, edit_group)):
        edit_group.id = random_group.id
        app.group.edit_group_by_id(edit_group)
    with pytest.allure.step('Then the new group list is equal to the old group list with edited group'):
        new_list_groups = db.get_list_groups()
        old_list_groups[index] = edit_group
        assert sorted(new_list_groups, key=Group.id_or_max) == sorted(old_list_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_list_groups, key=Group.id_or_max) == sorted(app.group.get_list_groups(), key=Group.id_or_max)

def test_group_list(app, db):
    def clean(group):
        return Group(id=group.id, name=re.sub(r'\s+', ' ', group.name.strip()))
    with pytest.allure.step('Verify sorted lists group from home page and database'):
        sorted_db_list = sorted(map(clean, db.get_list_groups()), key=Group.id_or_max)
        sorted_ui_list = sorted(app.group.get_list_groups(), key=Group.id_or_max)
        assert sorted_ui_list == sorted_db_list