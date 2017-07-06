# -*- coding: utf-8 -*-
from Training.model.group import Group


def test_Test_add_group(app):
    app.group.create(Group(name="New1", header="test123", footer="Test321"))

def test_Test_add_group_empty(app):
    app.group.create(Group (name="", header="", footer=""))




