import pytest
import json
from page_objects.burger_menu import BurgerMenu
from page_objects.inventory_page import InventoryPage
from page_objects.login_page import LoginPage
from page_objects.shoping_cart_page import ShoppingCart
from utilities.configurations import Configuration
from utilities.driver_factory import DriverFactory


# from Automation_tests.utilities.config_parser import ReadConfig


@pytest.fixture(scope="session")
def env():
    """
    Implementation a .json config
    """
    with open("configurations/configuration.json") as file:
        env_dict = json.loads(file.read())
    return Configuration(**env_dict)


@pytest.fixture()
def create_driver(env):
    # chrome_driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id()) # From ReadConfig
    chrome_driver = DriverFactory.create_driver(driver_id=env.browser_id)
    chrome_driver.maximize_window()
    # chrome_driver.get(ReadConfig.get_base_url()) # From ReadConfig
    chrome_driver.get(env.base_url)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def inventory_page(create_driver):
    return InventoryPage(create_driver)


@pytest.fixture()
def burger_menu(create_driver):
    return BurgerMenu(create_driver)


@pytest.fixture()
def shopping_cart(create_driver):
    return ShoppingCart(create_driver)
