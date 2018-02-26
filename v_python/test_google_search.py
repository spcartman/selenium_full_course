import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

test_url = 'http://localhost/litecart/admin/'
username = 'admin'
password = 'admin'

def update_input(wd, value, locator):
    input = wd.find_element_by_css_selector(locator)
    input.click()
    input.clear()
    input.send_keys(value)


def test_google_search(driver):
    driver.get(test_url)
    update_input(driver, username, 'input[name="username"]')
    update_input(driver, password, 'input[name="password"]')
    driver.find_element_by_name('login').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#box-apps-menu-wrapper')))
