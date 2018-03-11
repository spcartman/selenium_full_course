from importlib import import_module

data = import_module('data.data').test_data


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def admin_login(self, name, password):
        self.app.update_input(name, 'input[name="username"]')
        self.app.update_input(password, 'input[name="password"]')
        self.app.wd.find_element_by_name('login').click()
        self.app.wait_for_element_to_be_visible('#box-apps-menu-wrapper')

    def is_admin_logged_in(self):
        return len(self.app.wd.find_elements_by_css_selector('.fa-sign-out')) > 0

    def admin_smart_login(self):
        if not self.is_admin_logged_in():
            self.admin_login(self.app.admin_name, self.app.admin_password)

    def user_logout(self):
        self.app.wd.find_element_by_css_selector('a[href$="logout"]').click()
        self.app.wait_for_element_to_be_visible('#box-account-login')

    def user_smart_logout(self):
        if len(self.app.wd.find_elements_by_css_selector('a[href$="logout"]')) > 0:
            self.user_logout()

    def user_login(self, user):
        self.app.update_input(user.email, 'input[name="email"]')
        self.app.update_input(user.password, 'input[name="password"]')
        self.app.wd.find_element_by_css_selector('button[name="login"]').click()
        self.app.wait_for_element_to_be_visible('#box-account')

    def is_correct_user_logged_in(self, user):
        return self.app.wd.find_element_by_css_selector('div[class="notice success"]').text == \
               data['notifications']['successful_login'] % (user.f_name, user.l_name)
