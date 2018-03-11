def test_click_through_each_menu_and_submenu(app):
    app.navigation.go_to_admin_root()
    app.session.admin_smart_login()
    app.click_through_menu_and_submenu()
