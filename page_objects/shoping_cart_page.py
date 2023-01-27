from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage


class ShoppingCart(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __shopping_cart = (By.XPATH, "//*[@id='shopping_cart_container']")
    __your_cart = (By.XPATH, "//*[@id='header_container']//span")
    __your_cart_text = "YOUR CART"
    __add_to_cart_button = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    __item_in_shopping_cart = (By.CSS_SELECTOR, "#item_4_title_link")
    __name_of_item_in_shopping_item = "Sauce Labs Backpack"
    __checkout_button = (By.CSS_SELECTOR, "#checkout")
    __first_name_input = (By.CSS_SELECTOR, "#first-name")
    __last_name_input = (By.CSS_SELECTOR, "#last-name")
    __postal_code_input = (By.CSS_SELECTOR, "#postal-code")
    __continue_button = (By.XPATH, "//*[@id='continue']")
    __finish_button = (By.XPATH, "//*[@id='finish']")
    __complete_header = (By.XPATH, "//*[@id='checkout_complete_container']/h2")
    __complete_header_text = "THANK YOU FOR YOUR ORDER"
    __remove_from_shopping_cart_button = (By.XPATH, "//*[@id='remove-sauce-labs-backpack']")

    def open_shopping_cart(self):
        self._click(self.__shopping_cart)

    def your_cart(self):
        return self.read_text(self.__your_cart)

    def your_cart_text(self):
        return self.__your_cart_text

    def click_on_add_to_cart_button(self):
        self._click(self.__add_to_cart_button)

    def item_in_shopping_cart(self):
        return self.read_text(self.__item_in_shopping_cart)

    def name_of_item_in_shopping_item(self):
        return self.__name_of_item_in_shopping_item

    def click_on_checkout_button(self):
        self._click(self.__checkout_button)

    def set_credentials(self, first_name_value, last_name_value, postal_code_value):
        self._send_keys(self.__first_name_input, first_name_value)
        self._send_keys(self.__last_name_input, last_name_value)
        self._send_keys(self.__postal_code_input, postal_code_value)
        return self

    def click_on_continue_button(self):
        self._click(self.__continue_button)

    def click_on_finish_button(self):
        self._click(self.__finish_button)

    def complete_header(self):
        return self.read_text(self.__complete_header)

    def complete_header_text(self):
        return self.__complete_header_text

    def click_on_remove_from_shopping_cart_button(self):
        self._click(self.__remove_from_shopping_cart_button)
