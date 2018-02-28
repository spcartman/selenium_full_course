import pytest
from selenium import webdriver
from helpers import navigate_to_user_portal
from helpers import wait_for_element_to_be_visible
from helpers import is_expected_number_of_stickers_for_earch_product


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_number_of_stickers_on_each_product_matches_expected_value(driver):
    navigate_to_user_portal(driver)
    wait_for_element_to_be_visible(driver, '#box-most-popular')
    assert is_expected_number_of_stickers_for_earch_product(driver)
