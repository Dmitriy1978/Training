# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_Test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="New1", header="test123", footer="Test321"))
    app.logout()


def test_Test_add_group_empty(app):
    app.login(username="admin", password="secret")
    app.create_group(Group (name="", header="", footer=""))
    app.logout()



