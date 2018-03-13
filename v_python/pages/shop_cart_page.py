from selenium.webdriver.support.ui import WebDriverWait


class ShopCartPage:

    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    @property
    def items_carousel(self):
        return self.wd.find_element_by_css_selector('#box-checkout-cart')

    @property
    def items_in_cart(self):
        return self.items_carousel.find_elements_by_css_selector('.shortcut a')

    @property
    def item_names(self):
        return [i.text for i in self.wd.find_elements_by_css_selector('form[name="cart_form"] strong')]

    @property
    def remove_item_btns(self):
        return self.wd.find_elements_by_css_selector('button[name="remove_cart_item"]')

    @property
    def billing_address(self):
        return self.wd.find_element_by_css_selector('.billing-address')

    @property
    def summary(self):
        return self.wd.find_element_by_css_selector('#box-checkout-summary')

    @property
    def comments(self):
        return self.wd.find_element_by_css_selector('textarea[name="comments"]')

    @property
    def confirm_order_btn(self):
        return self.wd.find_element_by_css_selector('button[name="confirm_order"]')

    def get_item_names_from_summary(self):
        return [i.text for i in self.summary.find_elements_by_css_selector('td.item:nth-of-type(2)')]

    def wait_for_item_to_be_removed_from_order_summary(self, name):
        WebDriverWait(self.wd, 10).until(lambda x: name not in self.get_item_names_from_summary())

    def delete_all_items(self):
        count = len(self.items_in_cart)
        for i in range(count):
            # this check is needed since once one item remains in the cart carousel disappears
            if i + 1 < count:
                self.items_in_cart[0].click()
            self.app.wait_for_element_to_be_visible('button[name="remove_cart_item"]')  # wait for "Remove" button
            self.remove_item_btns[0].click()
            # this check is needed because summary panel disappears with last item deletion
            if i + 1 < count:
                self.wait_for_item_to_be_removed_from_order_summary(self.item_names[0])
        self.app.wait_for_element_to_be_visible('em')  # wait for empty cart text to appear

    def is_cart_empty(self):
        return len(self.item_names) == 0
