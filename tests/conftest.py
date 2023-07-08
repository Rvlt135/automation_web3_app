import pytest
from framework.api_client import ApiFunc


@pytest.fixture
def api_client():
    api_client = ApiFunc()
    return api_client
