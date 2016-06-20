# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest
import string

def random_string(prefix, maxlen):
    char = string.ascii_letters + string.hexdigits + ' '*15 #+ string.punctuation
    return prefix + "".join([random.choice(char) for i in range(random.randrange(maxlen))])

testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("Name_", 10)]
    for header in ["", random_string("Header_", 20)]
    for footer in ["", random_string("Footer_", 10)]
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_list_groups = app.group.get_list_groups()
    app.group.create(group)
    assert len(old_list_groups) + 1 == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups.append(group)
    assert sorted(new_list_groups, key=Group.id) == sorted(old_list_groups, key=Group.id)

def test_delete_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
    old_list_groups = app.group.get_list_groups()
    index = random.randrange(len(old_list_groups))
    app.group.delete_random_group(index)
    assert len(old_list_groups) - 1 == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups[index:index+1] = []
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
    index = random.randrange(len(old_list_groups))
    group.id = old_list_groups[index].id
    app.group.edit_random_group(index, group)
    assert len(old_list_groups) == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups[index] = group
    assert sorted(new_list_groups, key=Group.id) == sorted(old_list_groups, key=Group.id)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
    old_list_groups = app.group.get_list_groups()
    group = Group(header="Header_of_group_new")
    index = random.randrange(len(old_list_groups))
    group.id = old_list_groups[index].id
    app.group.edit_random_group(index, group)
    assert len(old_list_groups) == app.group.count()
    new_list_groups = app.group.get_list_groups()
    old_list_groups[index] = group
    assert sorted(new_list_groups, key=Group.id) == sorted(old_list_groups, key=Group.id)
