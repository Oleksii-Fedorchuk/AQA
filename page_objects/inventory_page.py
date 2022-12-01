from selenium.webdriver.common.by import By
from Automation_tests.utilities.web_ui.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __inventory_url = "https://www.saucedemo.com/inventory.html"
    __invalid_image = (By.XPATH, "//*[@src='/static/media/sl-404.168b1cce.jpg']")

    def get_invalid_image(self):
        return self.get_image(self.__invalid_image)

    def get_inventory_url(self):
        return self.__inventory_url
