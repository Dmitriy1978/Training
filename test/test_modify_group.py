from Training.model.group import Group


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test_add", header="new2", footer="new2"))
    app.group.modify_first_group(Group(name="New name Yes"))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test_add", header="new2", footer="new2"))
    app.group.modify_first_group(Group(header="New header"))


def test_modify_group_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group ( name="Test_add", header="new2", footer="new2"))
    app.group.modify_first_group(Group(footer="New footer"))

