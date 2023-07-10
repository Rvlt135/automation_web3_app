from framework.pages.base_page import BasePage
from framework.pages.metamask_auth_page import MetamaskAuthPage


class UIWorker(MetamaskAuthPage, BasePage):
    """Класс для работы со всеми экранами приложения"""
    # 'http://localhost:3000/'
    def open_app(self, url='http://localhost:3000/'):
        self.open_main_page(url)
