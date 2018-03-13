from selenium.webdriver.support.ui import WebDriverWait
from pages.shop_header_page import ShopHeaderPage


class ShopProductPage:

    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    @property
    def breadcrumbs(self):
        return self.wd.find_element_by_css_selector('#breadcrumbs')

    @property
    def title(self):
        return self.wd.find_element_by_css_selector('#box-product .title')

    @property
    def image(self):
        return self.wd.find_element_by_css_selector('.main-image')

    @property
    def image(self):
        return self.wd.find_element_by_css_selector('.main-image')

    @property
    def information(self):
        return self.wd.find_element_by_css_selector('div.information')

    @property
    def add_to_cart_btn(self):
        return self.information.find_element_by_css_selector('button[name="add_cart_product"]')

    @property
    def details(self):
        return self.information.find_element_by_css_selector('div.tabs')

    @property
    def similar_products_box(self):
        return self.information.find_element_by_css_selector('#box-similar-products')

    def add_product_to_cart(self):
        self.count_of_items_before = ShopHeaderPage(self.app).get_number_of_items_in_cart()
        self.add_to_cart_btn.click()
        self.wait_for_cart_items_counter_to_update()

    def wait_for_cart_items_counter_to_update(self):
        WebDriverWait(self.wd, 10).until\
            (lambda x: ShopHeaderPage(self.app).get_number_of_items_in_cart() - self.count_of_items_before == 1)
