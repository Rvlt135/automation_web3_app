import pytest
from framework.api_client import ApiFunctions
from blockchain_clients.w3_client import w3Polygon
from selenium import webdriver
from data.config import METAMSK_EXTENSION_FILE
from selenium.webdriver.chrome.options import Options

from framework.pages import UIWorker


@pytest.fixture
def api_client():
    api_client = ApiFunctions()
    return api_client


@pytest.fixture
def w3_client_polygon():
    w3_polygon = w3Polygon()
    return w3_polygon


@pytest.fixture
def driver():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument("--window-size=1920,1080")
    # driver = webdriver.Chrome(options=chrome_options)
    EXTENSION_PATH = METAMSK_EXTENSION_FILE
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension(EXTENSION_PATH)
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()


@pytest.fixture()
def pages(driver):
    """Воркер получает все экраны и работает с ними"""
    page = UIWorker(driver)
    page.open_main_page(url='http://localhost:3000/')
    return page
