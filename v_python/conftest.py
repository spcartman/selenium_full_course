import pytest
from fixture.fixture import Fixture


@pytest.fixture(scope="session")
def app(request):
    fixture = Fixture()
    request.addfinalizer(fixture.destroy)
    return fixture
