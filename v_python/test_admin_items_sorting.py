from importlib import import_module

data = import_module('test_data.data').test_data


def test_sorting_of_countries(app):
    app.navigate_to(data['url']['admin_countries'])
    app.safe_admin_login(data['credentials']['user'], data['credentials']['password'])
    countries = app.get_countries()
    assert countries == sorted(countries)
    non_zero_zones = app.get_countries_with_many_zones()
    for index in non_zero_zones:
        app.open_country_by_table_index(index)
        zones = app.get_zone_names()
        assert zones == sorted(zones)
        app.navigate_to(data['url']['admin_countries'])


def test_sorting_of_geo_zones(app):
    app.navigate_to(data['url']['admin_zones'])
    app.safe_admin_login(data['credentials']['user'], data['credentials']['password'])
    for index in range(app.get_number_of_geo_zone_countries()):
        app.open_geo_zone_country(index)
        zones = app.get_country_geo_zones()
        assert zones == sorted(zones)
        app.navigate_to(data['url']['admin_zones'])
