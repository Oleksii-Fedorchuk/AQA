from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __int__(self, driver):
        с = 0
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 5)

    __email_input_locator = (By.XPATH, "//input[@id='user-name']")
    __password_input_locator = (By.XPATH, "//input[@id='password']")

    def set_email(self, email_value):
        email_element = self._wait.until(EC.presence_of_element_located(self.__email_input_locator))
        email_element.clear()
        email_element.send_keys(email_value)

    def set_password(self, password_value):
        password_element = self._wait.until(EC.presence_of_element_located(self.__password_input_locator))
        password_element.clear()
        password_element.send_keys(password_value)
