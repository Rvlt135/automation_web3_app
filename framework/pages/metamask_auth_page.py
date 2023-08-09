import time
from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage
import framework.locators.locators_metamask as lc
from data.config import PASSWORD_METAMASK


class MetamaskInstall(BasePage):
    def first_page_auth_metamask(self):
        self.find_and_click(lc.check_box_terms_of_use)
        self.find_and_click(lc.button_import_an_exist_wallet)
        self.find_and_click(lc.button_i_agree_auth)

    def input_secret_recovery_value(self, secret_recovery_list: list):
        for index, value in enumerate(secret_recovery_list):
            locator = (By.CSS_SELECTOR, f'[data-testid="import-srp__srp-word-{index}"]')
            self.find_and_input(value, locator)
        self.find_and_click(lc.button_confirm_import)

    def input_password_and_confirm(self):
        self.find_and_input(PASSWORD_METAMASK, lc.new_password_input)
        self.find_and_input(PASSWORD_METAMASK, lc.new_password_repeat_input)
        self.find_and_click(lc.check_box_confirm_password)
        self.find_and_click(lc.button_confirm_import_wallet)
        self.find_and_click(lc.button_success_auth)
        self.find_and_click(lc.button_extension_next)
        self.find_and_click(lc.button_extension_done)

    def pop_up_notification(self):
        self.find_and_click_pop_up(lc.pop_up_notification)
        self.switch_window(1)
        # current_window_handle = self.driver.current_window_handle
        # for handle in self.driver.window_handles:
        #    if handle != current_window_handle:
        #        self.driver.switch_to.window(handle)
        #        break  # Переключились на первое всплывающее окно

        self.find_and_click(lc.pop_up_button_try_out)

    def settings_test_network(self):
        self.driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings')


    def switch_window_metamask(self):
        self.switch_window(1)
