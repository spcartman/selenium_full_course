import pytest
import json
from os import path
from fixture.fixture import Fixture


with open(path.join(path.dirname(path.abspath(__file__)), 'config.json')) as f:
    config = json.load(f)


@pytest.fixture(scope="session")
def app(request):
    fixture = Fixture(admin_root=config['admin']['url'],
                      admin_countries_url=config['admin']['countries_url'],
                      admin_zones_url=config['admin']['zones_url'],
                      admin_name=config['admin']['name'],
                      admin_password=config['admin']['password'],
                      shop_root=config['shop']['url'])
    request.addfinalizer(fixture.destroy)
    return fixture
