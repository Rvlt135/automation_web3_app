from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def find_and_click(self, locator, time=7):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)).click()

    def find_and_chek_text(self, locator, text, time=4):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text))

    def switch_window(self, win_number):
        switch_headless = self.driver.window_handles
        self.driver.switch_to.window(switch_headless[win_number])

    def find_and_click_pop_up(self, locator, time=5):
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator))

