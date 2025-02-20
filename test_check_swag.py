from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_saucedemo_icon():
    driver = webdriver.Chrome()  # Используем ChromeDriver

    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        icon_locator = (By.CLASS_NAME, "login_logo")
        icon_element = wait.until(EC.visibility_of_element_located(icon_locator))

        assert icon_element.is_displayed(), "Иконка не найдена на странице!"

        print("Тест пройден успешно! Иконка найдена.")

    except Exception as e:
        print(f"Тест завершился с ошибкой: {e}")

    finally:
        driver.quit()





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_saucedemo_username_field():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        driver.maximize_window()

        wait = WebDriverWait(driver, 10)
        username_locator = (By.ID, "user-name")
        username_field = wait.until(EC.visibility_of_element_located(username_locator))

        assert username_field.is_displayed(), "Поле для ввода имени пользователя не найдено на странице!"

        print("Тест пройден успешно! Поле для ввода имени пользователя найдено.")

    except Exception as e:
        print(f"Тест завершился с ошибкой: {e}")

    finally:
        driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_saucedemo_password_field():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        driver.maximize_window()

        wait = WebDriverWait(driver, 10)
        password_locator = (By.ID, "password")
        password_field = wait.until(EC.visibility_of_element_located(password_locator))

        assert password_field.is_displayed(), "Поле для ввода пароля не найдено на странице!"

        print("Тест пройден успешно! Поле для ввода пароля найдено.")

    except Exception as e:
        print(f"Тест завершился с ошибкой: {e}")

    finally:
        driver.quit()
