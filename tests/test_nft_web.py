import allure
import time
import logging


def test_check_main_page(pages):
    pages.open_app()
    time.sleep(10)
