class ShopHelper:

    def __init__(self, app):
        self.app = app

    def click_create_account_link(self):
        self.app.wd.find_element_by_css_selector('.account a[href$="create_account"]').click()
        self.app.wait_for_element_to_be_visible('form[name="customer_form"]')

    def fill_new_user_form(self, user):
        self.app.update_input(user.f_name, 'input[name="firstname"]')
        self.app.update_input(user.l_name, 'input[name="lastname"]')
        self.app.update_input(user.address, 'input[name="address1"]')
        self.app.update_input(user.postcode, 'input[name="postcode"]')
        self.app.update_input(user.city, 'input[name="city"]')
        self.app.wd.find_element_by_css_selector('.select2-selection__rendered').click()
        self.app.wd.find_element_by_css_selector('li[id$="-%s"]' % user.country).click()
        self.app.update_input(user.email, 'input[name="email"]')
        self.app.update_input(user.phone, 'input[name="phone"]')
        self.app.update_input(user.password, 'input[name="password"]')
        self.app.update_input(user.password, 'input[name="confirmed_password"]')

    def click_create_account_button(self):
        self.app.wd.find_element_by_css_selector('button[name="create_account"]').click()
        self.app.wait_for_element_to_be_visible('a[href$="logout"]')

    def create_user(self, user):
        self.click_create_account_link()
        self.fill_new_user_form(user)
        self.click_create_account_button()
