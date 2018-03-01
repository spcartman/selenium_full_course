from importlib import import_module

data = import_module('test_data.data').test_data


def test_click_through_each_menu_and_submenu(app):
    app.navigate_to(data['url']['admin_root'])
    app.safe_admin_login(data['credentials']['user'], data['credentials']['password'])
    app.click_through_menu_and_submenu()
