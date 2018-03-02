from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from model.duck import Duck


class Fixture:

    def __init__(self, browser='Chrome'):
        if browser == 'Chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'Firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'IE':
            self.wd = webdriver.Ie()
        elif browser == 'Safari':
            self.wd = webdriver.Safari()
        else:
            raise ValueError('Unrecognized browser "%s"' % browser)

    def destroy(self):
        self.wd.quit()

    def navigate_to(self, url):
        if not self.wd.current_url == url:
            self.wd.get(url)

    def wait_for_element_to_be_visible(self, locator):
        WebDriverWait(self.wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    def update_input(self, value, locator):
        input = self.wd.find_element_by_css_selector(locator)
        input.click()
        input.clear()
        input.send_keys(value)

    def admin_login(self, user, password):
        self.update_input(user, 'input[name="username"]')
        self.update_input(password, 'input[name="password"]')
        self.wd.find_element_by_name('login').click()
        self.wait_for_element_to_be_visible('#box-apps-menu-wrapper')

    def is_admin_logged_in(self):
        return len(self.wd.find_elements_by_css_selector('.fa-sign-out')) > 0

    def safe_admin_login(self, user, password):
        if not self.is_admin_logged_in():
            self.admin_login(user, password)

    def click_through_menu_and_submenu(self):
        for i in range(len(self.wd.find_elements_by_css_selector('li#app-'))):
            self.wd.find_elements_by_css_selector('li#app-')[i].click()
            self.wait_for_element_to_be_visible('h1')
            for j in range(len(self.wd.find_elements_by_css_selector('li[id^=doc]'))):
                self.wd.find_elements_by_css_selector('li[id^=doc]')[j].click()
                self.wait_for_element_to_be_visible('h1')

    def is_expected_number_of_stickers_for_earch_product(self, number):
        for product in self.wd.find_elements_by_css_selector('li.product'):
            if len(product.find_elements_by_css_selector('div[class^=sticker]')) != number:
                return False
        return True

    def get_countries(self):
        return [i.text for i in self.wd.find_elements_by_css_selector('a[href*="country_code"]:not([title="Edit"])')]

    def get_countries_with_many_zones(self):
        zones = [int(i.text) for i in self.wd.find_elements_by_xpath('//tr[@class="row"]/td[6]')]
        table_indices_of_non_zero_zones = [i + 1 for i in range(len(zones)) if zones[i] > 0]
        return table_indices_of_non_zero_zones

    def open_country_by_table_index(self, index):
        self.wd.find_element_by_xpath('//tr[@class="row"][%s]//a' % str(index)).click()
        self.wait_for_element_to_be_visible('#table-zones')

    def get_zone_names(self):
        return [i.get_attribute('value') for i in self.wd.find_elements_by_css_selector('[name$="][name]"]')]

    def get_number_of_geo_zone_countries(self):
        return len(self.wd.find_elements_by_css_selector('tr.row'))

    def open_geo_zone_country(self, index):
        self.wd.find_element_by_xpath('//tr[@class="row"][%s]//a' % str(index + 1)).click()
        self.wait_for_element_to_be_visible('#table-zones')

    def get_country_geo_zones(self):
        return [i.text for i in self.wd.find_elements_by_css_selector('select[name$="[zone_code]"] option[selected]')]

    def get_campaigns_first_duck(self):
        duck = self.wd.find_elements_by_css_selector('#box-campaigns .product')[0]
        name = duck.find_element_by_css_selector('.name').text
        reg_price = duck.find_element_by_css_selector('.regular-price').text[1:]  # strip "$" sign
        sale_price = duck.find_element_by_css_selector('.campaign-price').text[1:]  # strip "$" sign
        return Duck(name=name, reg_price=reg_price, sale_price=sale_price)

    def open_campaigns_first_duck(self):
        self.wd.find_elements_by_css_selector('#box-campaigns .product')[0].click()
        self.wait_for_element_to_be_visible('#box-product')

    def get_duck_details(self):
        duck = self.wd.find_element_by_css_selector('#box-product')
        name = duck.find_element_by_css_selector('.title').text
        reg_price = duck.find_element_by_css_selector('.regular-price').text[1:]  # strip "$" sign
        sale_price = duck.find_element_by_css_selector('.campaign-price').text[1:]  # strip "$" sign
        return Duck(name=name, reg_price=reg_price, sale_price=sale_price)

    def get_price_styles(self, locator):
        price = self.wd.find_element_by_css_selector(locator)
        tag = price.get_attribute('localName')
        bold = tag == 'strong'
        strike = tag == 's'
        colour = price.value_of_css_property('color')
        font_size = float(price.value_of_css_property('font-size')[:-2])
        return {'bold': bold, 'strike': strike, 'colour': colour, 'font_size': font_size}

    def get_landing_reg_price_style(self):
        return self.get_price_styles('#box-campaigns .regular-price')

    def get_landing_sale_price_style(self):
        return self.get_price_styles('#box-campaigns .campaign-price')

    def get_details_reg_price_style(self):
        return self.get_price_styles('.regular-price')

    def get_details_sale_price_style(self):
        return self.get_price_styles('.campaign-price')

    def is_price_colour_of_expected_colour(self, style, colour):
        rgba_num_array = style['colour'].strip('rgba()').split(',')
        if colour == 'gray':
            return int(rgba_num_array[0]) == int(rgba_num_array[1]) == int(rgba_num_array[2])
        elif colour == 'red':
            return int(rgba_num_array[1]) == int(rgba_num_array[2]) == 0
        return False
