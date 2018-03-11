from importlib import import_module

data = import_module('data.data').test_data


def test_number_of_stickers_on_each_product_matches_expected_value(app):
    app.navigation.go_to_shop_root()
    assert app.is_expected_number_of_stickers_for_earch_product(data['misc']['expected_number_of_stickers_for_earch_product'])
