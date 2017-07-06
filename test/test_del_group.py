# -*- coding: utf-8 -*-
from Training.model.group import Group
from Training.fixture.group import GroupHelper
from Training.fixture.session import SessionHelper
from Training.fixture.application import Application


def test_delete_first_group(app):
    app.group.delete_first_group()
