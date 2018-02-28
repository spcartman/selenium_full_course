from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

test_url = 'http://localhost/litecart/admin/'
username = 'admin'
password = 'admin'


def navigate_to_admin_portal(driver):
    driver.get(test_url)


def update_input(wd, value, locator):
    input = wd.find_element_by_css_selector(locator)
    input.click()
    input.clear()
    input.send_keys(value)


def admin_login(driver):
    update_input(driver, username, 'input[name="username"]')
    update_input(driver, password, 'input[name="password"]')
    driver.find_element_by_name('login').click()


def wait_for_element_to_be_visible(driver, locator):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
