from selenium.webdriver.common.by import By
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://demoqa.com/'

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_url(self):
        return self.driver.current_url



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'

    def visit(self):
        """Переход на главную страницу"""
        self.driver.get(self.base_url)

    def find_element(self, locator):
        """Поиск элемента на странице"""
        by, value = locator
        return self.driver.find_element(by, value)
