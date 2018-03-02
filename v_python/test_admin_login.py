# import pytest
# from selenium import webdriver
# from helpers import admin_login
# from helpers import navigate_to_admin_portal
# from helpers import wait_for_element_to_be_visible
#
#
# @pytest.fixture
# def driver(request):
#     wd = webdriver.Chrome()
#     # wd = webdriver.Firefox()
#     # wd = webdriver.Safari()
#     # wd = webdriver.Firefox(capabilities={'marionette': False},
#     #                        firefox_binary='/Applications/Firefoxx.app/Contents/MacOS/firefox-bin')
#     # wd = webdriver.Firefox(firefox_binary='/Applications/FirefoxNightly.app/Contents/MacOS/firefox')
#     print(wd.capabilities)
#     request.addfinalizer(wd.quit)
#     return wd
#
#
# def test_valid_admin_login(driver):
#     navigate_to_admin_portal(driver)
#     admin_login(driver)
#     wait_for_element_to_be_visible(driver, '#box-apps-menu-wrapper')


from importlib import import_module

data = import_module('test_data.data').test_data


def test_valid_admin_login(app):
    app.navigate_to(data['url']['admin_root'])
    app.safe_admin_login(data['credentials']['user'], data['credentials']['password'])
