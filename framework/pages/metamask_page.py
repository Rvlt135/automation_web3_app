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

    def switch_window_metamask(self):
        self.switch_window(1)


class MetaMaskPages(BasePage):

    def add_settings_test_network(self, setting_test_net_list):
        self.driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network')
        for index, value in enumerate(setting_test_net_list, start=1):
            locator = (
                By.CSS_SELECTOR, f'.networks-tab__add-network-form-body > div:nth-child({index}) > label > input')
            self.find_and_input(value, locator, time=7)
        self.find_and_click(lc.button_save_test_net)
        self.switch_window(1)
        self.find_and_click(lc.change_test_net_button)
        self.driver.close()
        self.switch_window(0)
        self.driver.refresh()
        time.sleep(10)

    def work_to_metamask_extension(self):
        js_script_click_button_next_metamask = """
        var connectButton = document.querySelector('[data-testid="page-container-footer-next"]');
        if (connectButton) {
        connectButton.click();
        }
        """

        # Получить список всех окон
        window_handles = self.get_all_window_handles()

        # Вывести количество окон в консоль
        print("Количество доступных окон:", len(window_handles))
        self.driver.execute_script(js_script_click_button_next_metamask)
        self.switch_window(0)
        self.driver.refresh()
        time.sleep(7)