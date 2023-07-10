import allure
import time
import logging
from data.config import TYPE_SECRET_PHRASE_LIST


def test_check_main_page(pages):
    pages.open_app()
    # time.sleep(5)
    # pages.first_auth_metamask(TYPE_SECRET_PHRASE_LIST)


def test_auth_metamask(pages):
    pages.switch_window_metamask()
    pages.first_page_auth_metamask()
    pages.input_secret_recovery_value(TYPE_SECRET_PHRASE_LIST)
    pages.input_password_and_confirm()

