from os import path
from random import randrange
from selenium.webdriver.support.ui import Select


def get_img_abs_path():
    # string slicing is needed to get rid of "WebDriverException: Message: unknown error: path is not canonical" error
    # because it cannot handle path like '/User/name/folder_0/../folder_1/img.jpg'
    return path.join(path.dirname(path.abspath(__file__))[:-4], 'resources/img.jpg')


def test_add_new_product(app):
    app.navigation.go_to_catalog()
    app.session.admin_smart_login()

    # switch to "General" tab
    app.wd.find_element_by_css_selector('a[href$="&doc=edit_product"]').click()  # click "Add New Product" button
    app.wait_for_element_to_be_visible('#tab-general')  # wait for "General" tab to be visible

    # fill "General" tab
    app.wd.find_element_by_css_selector('input[type="radio"][value="1"]').click()  # set "Status" to "Enabled"
    product_name = 'product_' + str(randrange(100000))
    app.update_input(product_name, 'input[name="name[en]"]')  # enter product "Name"
    app.update_input('code_' + str(randrange(100000)), 'input[name="code"]')  # enter product "Code"
    app.wd.find_element_by_css_selector('input[data-name="Subcategory"]').click()  # check "Subcategory"
    app.wd.find_element_by_css_selector('input[value="1-3"]').click()  # check "Unisex"
    app.update_input(str(randrange(50)), 'input[name="quantity"]')  # enter product "Quantity"
    sold_out_dropdown = Select(app.wd.find_element_by_css_selector('select[name="sold_out_status_id"]'))
    sold_out_dropdown.select_by_value('2')  # set "Sold Out Status" to "Temporary sold out"
    app.wd.find_element_by_css_selector('input[name="new_images[]"]').send_keys(get_img_abs_path())  # upload image
    app.wd.find_element_by_css_selector('input[name="date_valid_from"]').send_keys('30/11/2014')  # enter product "Date Valid From"
    app.wd.find_element_by_css_selector('input[name="date_valid_to"]').send_keys('14/03/2019')  # enter product "Date Valid To"

    # switch to "Information" tab
    app.wd.find_element_by_css_selector('a[href$="tab-information"]').click()  # switch to "Information" tab
    app.wait_for_element_to_be_visible('#tab-information')  # wait for "Information" tab to be visible

    # fill "Information" tab
    manufacturer_dropdown = Select(app.wd.find_element_by_css_selector('select[name="manufacturer_id"]'))
    manufacturer_dropdown.select_by_value('1')  # set "Manufacturer" to "ACME Corp."
    app.update_input('keywords_' + str(randrange(100000)), 'input[name="keywords"]')  # enter product "Keywords"
    app.update_input('short descr_' + str(randrange(100000)), 'input[name="short_description[en]"]')  # enter product "Short Description"
    app.update_input('long descr_' + str(randrange(100000)), 'div.trumbowyg-editor')  # enter product "Description"
    app.update_input('head title_' + str(randrange(100000)), 'input[name="head_title[en]"]')  # enter product "Head Title"
    app.update_input('mete descr_' + str(randrange(100000)), 'input[name="meta_description[en]"]')  # enter product "Meta Description"

    # switch to "Prices" tab
    app.wd.find_element_by_css_selector('a[href$="tab-prices"]').click()  # switch to "Prices" tab
    app.wait_for_element_to_be_visible('#tab-prices')  # wait for "Prices" tab to be visible

    # fill "Prices" tab
    purchase_price = randrange(10, 1000)
    app.update_input(str(purchase_price), 'input[name="purchase_price"]')  # enter product "Purchase Price"
    price_dropdown = Select(app.wd.find_element_by_css_selector('select[name="purchase_price_currency_code"]'))
    price_dropdown.select_by_value('EUR')  # set price to "Euros"
    app.update_input(str((purchase_price + 10) * 1.23), 'input[name="prices[USD]"]')  # enter price in USD
    app.update_input(str(purchase_price + 10), 'input[name="prices[EUR]"]')  # enter price in EUR

    # save product
    app.wd.find_element_by_css_selector('button[name="save"]').click()  # click "Save" button
    app.wait_for_element_to_be_visible('form[name="catalog_form"]')  # wait for products list to be visible

    # check that product is created and is in the list of products
    list_of_products = [i.text for i in app.wd.find_elements_by_css_selector('.dataTable td:nth-of-type(3) a')]
    assert product_name in list_of_products
