import time

from data.config import (TYPE_SECRET_PHRASE_LIST, SETTINGS_METAMASK_TEST_NET_LIST)


def test_check_main_page(pages):
    pages.open_app()


def test_auth_metamask(pages):
    pages.switch_window_metamask()
    pages.first_page_auth_metamask()
    pages.input_secret_recovery_value(TYPE_SECRET_PHRASE_LIST)
    pages.input_password_and_confirm()
    pages.add_settings_test_network(SETTINGS_METAMASK_TEST_NET_LIST)
    pages.work_to_metamask_extension()

