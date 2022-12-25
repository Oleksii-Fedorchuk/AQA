from selenium.webdriver.common.by import By
from Automation_tests.utilities.web_ui.base_page import BasePage
from CONSTANTS import main_page_url, title_name, inventory_page_url
from Automation_tests.utilities.config_parser import ReadConfig


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __email_input = (By.XPATH, "//input[@id='user-name']")
    __password_input = (By.XPATH, "//input[@id='password']")
    __login_button = (By.XPATH, "//*[@id='login-button']")
    __login_error = (By.XPATH, "//*[@data-test='error']")

    @property
    def login_page_title(self):
        return main_page_url.title()

    @property
    def inventory_page_url(self):
        return inventory_page_url

    @property
    def login_page_url(self):
        return main_page_url

    @property
    def title_name(self):
        return title_name

    def login(self, email_value):
        self._send_keys(self.__email_input, email_value)
        self._send_keys(self.__password_input, ReadConfig.get_password())
        self._click(self.__login_button)

    def _is_login_error_text(self):
        return self.read_text(self.__login_error)


