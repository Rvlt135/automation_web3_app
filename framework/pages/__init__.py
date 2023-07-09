from framework.pages.main_page import BasePage


class UIWorker(BasePage):
    """Класс для работы со всеми экранами приложения"""

    def open_app(self, url='http://localhost:3000/'):
        self.open_main_page(url)
