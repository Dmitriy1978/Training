# -*- coding: utf-8 -*-
import pytest

from Training.fixture.application import Application
from Training.model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_Test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="New1", header="test123", footer="Test321"))
    app.session.logout()


def test_Test_add_group_empty(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group (name="", header="", footer=""))
    app.session.logout()



