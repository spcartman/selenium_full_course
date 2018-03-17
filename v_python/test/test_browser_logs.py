def test_print_browser_logs(app):
    app.navigation.go_to_catalog_first_category()
    app.session.admin_smart_login()
    app.admin_catalog.go_though_each_product_and_print_browser_log()
