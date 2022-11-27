import pytest
from Automation_tests.page_objects.login_page import LoginPage
from Automation_tests.utilities.config_parser import ReadConfig
from Automation_tests.utilities.friver_factory import DriverFactory
from selenium.webdriver.support.wait import WebDriverWait


# @pytest.fixture()
# def create_wait_object(create_driver):
#     return WebDriverWait(create_driver, 5)


@pytest.fixture()
def create_driver():
    chrome_driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id())
    chrome_driver.maximize_window()
    chrome_driver.get(ReadConfig.get_base_url())
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)

