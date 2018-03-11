def test_sorting_of_countries(app):
    app.navigation.go_to_admin_countries()
    app.session.admin_smart_login()
    countries = app.get_countries()
    assert countries == sorted(countries)
    non_zero_zones = app.get_countries_with_many_zones()
    for index in non_zero_zones:
        app.open_country_by_table_index(index)
        zones = app.get_zone_names()
        assert zones == sorted(zones)
        app.navigation.go_to_admin_countries()


def test_sorting_of_geo_zones(app):
    app.navigation.go_to_admin_zones()
    app.session.admin_smart_login()
    for index in range(app.get_number_of_geo_zone_countries()):
        app.open_geo_zone_country(index)
        zones = app.get_country_geo_zones()
        assert zones == sorted(zones)
        app.navigation.go_to_admin_zones()
