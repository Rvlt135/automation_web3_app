import time

from framework.pages.base_page import BasePage
import framework.locators.locators_metamask as lc


class MetamaskAuthPage(BasePage):
    def first_page_auth_metamask(self):
        self.find_and_click(lc.check_box_terms_of_use)
        self.find_and_click(lc.button_import_an_exist_wallet)

    def input_secret_recovery_value(self, secret_recovery_list: list):
        for i in secret_recovery_list:
            self.find_and_input(i, lc.secret_recovery_1)
            self.find_and_input(i, lc.secret_recovery_2)
            # self.fill_metamask_recover_fields(secret_recovery_list)

    def input_password_and_confirm(self):
        self.find_and_input('TestMetamask1234', lc.new_password_input)
        self.find_and_click(lc.button_confirm_import)
        self.find_and_input('TestMetamask1234', lc.new_password_input)
        self.find_and_input('TestMetamask1234', lc.new_password_repeat_input)
        self.find_and_click(lc.check_box_confirm_password)
        self.find_and_click(lc.button_confirm_import)
        self.find_and_click(lc.button_success_auth)

    def switch_window_metamask(self):
        time.sleep(2)
        self.switch_window()
