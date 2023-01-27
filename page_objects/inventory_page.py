from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __inventory_url = "https://www.saucedemo.com/inventory.html"
    __invalid_image = (By.XPATH, "//*[@src='/static/media/sl-404.168b1cce.jpg']")

    @property
    def get_inventory_url(self):
        return self.__inventory_url
