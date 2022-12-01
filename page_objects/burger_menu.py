from selenium.webdriver.common.by import By
from Automation_tests.utilities.web_ui.base_page import BasePage


class BurgerMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __burger_menu = (By.XPATH, "//*[@id='react-burger-menu-btn']")
    __all_items = (By.XPATH, "//*[@id='inventory_sidebar_link']")
    __about = (By.XPATH, "//*[@id='about_sidebar_link']")
    __logout = (By.XPATH, "//*[@id='logout_sidebar_link']")
    __reset_app_state = (By.XPATH, "//*[@id='reset_sidebar_link']")
    __about_url = "https://saucelabs.com/"
    __text_all_items = "ALL ITEMS"

    def get_burger_menu(self):
        return self._click(self.__burger_menu)

    def get_all_items(self):
        return self.__all_items

    def get_about(self):
        return self.__about

    def get_logout(self):
        return self.__logout

    def get_reset_app_state(self):
        return self.__reset_app_state

    def get_text(self, burger_menu_item):
        return self.read_text(burger_menu_item)

    def click_on(self, burger_menu_item):
        return self._click(burger_menu_item)

    def about_url(self):
        return self.__about_url

    def all_items_text(self):
        return self.__text_all_items
