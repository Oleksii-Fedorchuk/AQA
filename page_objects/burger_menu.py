import time

from selenium.webdriver.common.by import By
from Automation_tests.utilities.web_ui.base_page import BasePage
from CONSTANTS import about_url


class BurgerMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __burger_menu = (By.XPATH, "//*[@id='react-burger-menu-btn']")
    __about = (By.XPATH, "//*[@id='about_sidebar_link']")
    __logout = (By.XPATH, "//*[@id='logout_sidebar_link']")
    __menu_button_container = (By.XPATH, '//*[@id="menu_button_container"]/div/div/div/nav/a')

    def open_burger_menu(self):
        return self._click(self._wait_until_element_located(self.__burger_menu)), time.sleep(0.5)

    def list_of_burger_menu(self):
        list_of_burger_menu = []
        elements = self._wait_until_elements_located(self.__menu_button_container)
        for element in elements:
            list_of_burger_menu.append(element.text)
        return list_of_burger_menu

    def click_on_about(self):
        self._click(self._wait_until_element_located(self.__about))

    @property
    def about_url(self):
        return about_url

    def click_logout_button(self):
        self._click(self._wait_until_element_located(self.__logout))
