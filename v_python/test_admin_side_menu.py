import pytest
from selenium import webdriver
from helpers import admin_login
from helpers import navigate_to_admin_portal
from helpers import wait_for_element_to_be_visible


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_valid_admin_login(driver):
    navigate_to_admin_portal(driver)
    admin_login(driver)
    wait_for_element_to_be_visible(driver, '#box-apps-menu-wrapper')

    for i in range(len(driver.find_elements_by_css_selector('li#app-'))):
        driver.find_elements_by_css_selector('li#app-')[i].click()
        wait_for_element_to_be_visible(driver, 'h1')
        for j in range(len(driver.find_elements_by_css_selector('li[id^=doc]'))):
            driver.find_elements_by_css_selector('li[id^=doc]')[j].click()
            wait_for_element_to_be_visible(driver, 'h1')
