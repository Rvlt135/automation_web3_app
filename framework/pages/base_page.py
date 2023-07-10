import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator))

    def find_and_input(self, text: str, locator: str, time=5):
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)).send_keys(text)

    def find_and_click(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)).click()

    def find_and_chek_text(self, locator, text, time=4):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text))

    def fill_metamask_recover_fields(self, fields, time=4):
        field_prefix = "import-srp__srp-word-"
        # num_fields = len(secret_phrase_field_values)
        # for i in range(num_fields):
        # field_locator = f"[data-testid=import-srp__srp-word-{i}']"
        # field_value = secret_phrase_field_values[i]
        for selector, value in fields.items():
            WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector))).send_keys(value)
            time.sleep(3)
            # return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(
            #    (By.CSS_SELECTOR, field_locator))).send_keys(field_value)

            # return self.find_and_input(field_value, field_locator)

    def switch_window(self):
        switch_headless = self.driver.window_handles
        self.driver.switch_to.window(switch_headless[1])
