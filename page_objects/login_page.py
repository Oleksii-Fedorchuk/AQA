from selenium.webdriver.common.by import By
from Automation_tests.data.error_data import locked_error_on_login_page
from Automation_tests.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_url = "https://www.saucedemo.com/"
    __email_input = (By.XPATH, "//input[@id='user-name']")
    __password_input = (By.XPATH, "//input[@id='password']")
    __login_button = (By.XPATH, "//*[@id='login-button']")
    __login_error = (By.XPATH, "//*[@data-test='error']")
    __get_locked_error = locked_error_on_login_page
    __title = "Swag Labs"

    def login_page_url(self):
        return self.__login_url

    def set_email(self, email_value):
        self._send_keys(self.__email_input, email_value)
        return self

    def set_password(self, password_value):
        self._send_keys(self.__password_input, password_value)
        return self

    def click_login_button(self):
        self._click(self.__login_button)

    def _is_login_error_text_displayed(self):
        return self.is_displayed(self.__login_error)

    def get_text(self):
        return self.read_text(self.__login_error)

    def get_locked_error(self):
        return self.__get_locked_error

    def get_title(self):
        return self.__title
