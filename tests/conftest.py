import pytest
from framework.api_client import ApiFunctions
from blockchain_clients.w3_client import w3Polygon


@pytest.fixture
def api_client():
    api_client = ApiFunctions()
    return api_client


@pytest.fixture
def w3_client_polygon():
    w3_polygon = w3Polygon()
    return w3_polygon
