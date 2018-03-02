from importlib import import_module

data = import_module('test_data.data').test_data


def test_landing_product_matches_product_details(app):
    app.navigate_to(data['url']['portal_root'])
    landing_duck = app.get_campaigns_first_duck()
    app.open_campaigns_first_duck()
    details_duck = app.get_duck_details()
    assert landing_duck == details_duck


def test_product_prices_styles(app):
    app.navigate_to(data['url']['portal_root'])
    landing_reg_price_style = app.get_landing_reg_price_style()
    landing_sale_price_style = app.get_landing_sale_price_style()
    app.open_campaigns_first_duck()
    details_reg_price_style = app.get_details_reg_price_style()
    details_sale_price_style = app.get_details_sale_price_style()
    assert landing_reg_price_style['strike'] == details_reg_price_style['strike'] == True
    assert landing_sale_price_style['bold'] == details_sale_price_style['bold'] == True
    assert landing_sale_price_style['font_size'] > landing_reg_price_style['font_size']
    assert details_sale_price_style['font_size'] > details_reg_price_style['font_size']
    assert app.is_price_colour_of_expected_colour(landing_reg_price_style, data['styles']['colour']['reg'])
    assert app.is_price_colour_of_expected_colour(landing_sale_price_style, data['styles']['colour']['sale'])
    assert app.is_price_colour_of_expected_colour(details_reg_price_style, data['styles']['colour']['reg'])
    assert app.is_price_colour_of_expected_colour(details_sale_price_style, data['styles']['colour']['sale'])
