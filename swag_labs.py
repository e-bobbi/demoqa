from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class SwagLabs(BasePage):
    def exist_icon(self):
        """
        Проверяем наличие элемента с локатором 'div.login_logo'.
        Возвращаем True, если элемент существует, иначе False.
        """
        try:
            self.find_element((By.CSS_SELECTOR, 'div.login_logo'))
            return True
        except NoSuchElementException:
            return False
