from pages.shop_product_page import ShopProductPage


class ShopMainPage:

    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def open(self):
        self.app.navigation.go_to_shop_root()

    @property
    def hero_image(self):
        return self.wd.find_element_by_css_selector('#slider-wrapper')

    @property
    def most_popular_box(self):
        return self.wd.find_element_by_css_selector('#box-most-popular')

    @property
    def most_popular_products(self):
        return self.most_popular_box.find_elements_by_css_selector('.product')

    @property
    def campaigns_box(self):
        return self.wd.find_element_by_css_selector('#box-campaigns')

    @property
    def latest_products_box(self):
        return self.wd.find_element_by_css_selector('#box-latest-products')

    def open_first_product(self):
        self.most_popular_products[0].click()
        self.app.wait_for_element_to_be_visible('#box-product')  # wait for product box to be visible

    def add_n_products_to_cart(self, n):
        for i in range(n):
            self.open()
            self.open_first_product()
            ShopProductPage(self.app).add_product_to_cart()
