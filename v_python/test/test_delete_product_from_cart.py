from pages.shop_cart_page import ShopCartPage
from pages.shop_header_page import ShopHeaderPage
from pages.shop_main_page import ShopMainPage
from importlib import import_module

number_of_products_to_add = import_module('data.data').test_data['misc']['number_of_products_to_add_to_cart']


def test_delete_product_from_cart(app):
    header = ShopHeaderPage(app)
    main_page = ShopMainPage(app)
    cart_page = ShopCartPage(app)

    main_page.open()
    main_page.add_n_products_to_cart(number_of_products_to_add)
    header.open_cart()
    cart_page.delete_all_items()

    assert cart_page.is_cart_empty()
