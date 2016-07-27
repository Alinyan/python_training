from pytest_bdd import given, when, then
from model.group import Group
import random

@given('a group list')
def group_list(db):
    return db.get_list_groups()

@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)

@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_list_groups()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_list_groups()) == 0:
        app.group.create(Group(name="name_group123"))
    return db.get_list_groups()

@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)

@then('the new group list is equal to the old group list without the deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_list_groups()
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_list_groups(), key=Group.id_or_max)

@given('a index of the edited group')
def index_group(non_empty_group_list, random_group):
    return non_empty_group_list.index(random_group)

@when('I edit the group from the list')
def edit_group(app, new_group, random_group):
    new_group.id = random_group.id
    app.group.edit_group_by_id(new_group)

@then('the new group list is equal to the old group list with edited group')
def verify_group_edited(db, non_empty_group_list, new_group, index_group, app, check_ui):
    old_lists = non_empty_group_list
    new_lists = db.get_list_groups()
    old_lists[index_group] = new_group
    assert sorted(new_lists, key=Group.id_or_max) == sorted(old_lists, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_lists, key=Group.id_or_max) == sorted(app.group.get_list_groups(), key=Group.id_or_max)
