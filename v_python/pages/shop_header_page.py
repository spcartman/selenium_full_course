class ShopHeaderPage:

    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    @property
    def logo(self):
        return self.wd.find_element_by_css_selector('#logotype-wrapper')

    @property
    def region(self):
        return self.wd.find_element_by_css_selector('#region')

    @property
    def cart(self):
        return self.wd.find_element_by_css_selector('#cart')

    @property
    def cart_items_count(self):
        return self.cart.find_element_by_css_selector('.quantity')

    @property
    def customer_service(self):
        return self.wd.find_element_by_css_selector('#customer-service-wrapper')

    def get_number_of_items_in_cart(self):
        return int(self.cart_items_count.text)

    def open_cart(self):
        self.cart.click()
        self.app.wait_for_element_to_be_visible('#customer-service-wrapper')  # wait for customer service to be visible
