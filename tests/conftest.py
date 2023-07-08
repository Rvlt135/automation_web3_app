import pytest
from framework.api_client import ApiFunctions


@pytest.fixture
def api_client():
    api_client = ApiFunctions()
    return api_client


@pytest.fixture
def w3_client():
    pass