from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Automation_tests.utilities.config_parser import ReadConfig


def test_1(open_login_page):
    login_page = open_login_page
    login_page.set_email(ReadConfig.get_standard_user_name())
    login_page.set_password(ReadConfig.get_password())


def test_title(create_driver):
    chrome_driver = create_driver
    actual_title = chrome_driver.title
    assert actual_title == "Swag Labs"


def test_login_as_standard_user():
    """Pre_set_up"""
    user_name = "standard_user"
    password = "secret_sauce"
    chrome_driver = Chrome("Automation_tests/utilities/chromedriver")
    chrome_driver.get("https://www.saucedemo.com")
    """Email_input"""
    email_input_locator = "//input[@id='user-name']"
    email_input_element = chrome_driver.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_name)
    """Password_input"""
    password_input_locator = "//input[@id='password']"
    password_input_element = chrome_driver.find_element(By.XPATH, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    """Login_button"""
    login_button_locator = "//*[@id='login-button']"
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    actual_result = "https://www.saucedemo.com/inventory.html"
    assert actual_result == "https://www.saucedemo.com/inventory.html"


def test_login_as_locked_user():
    """Pre_set_up"""
    user_name = "locked_out_user"
    password = "secret_sauce"
    chrome_driver = Chrome("Automation_tests/utilities/chromedriver")
    chrome_driver.get("https://www.saucedemo.com")
    """Email_input"""
    email_input_locator = "//input[@id='user-name']"
    email_input_element = chrome_driver.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_name)
    """Password_input"""
    password_input_locator = "//input[@id='password']"
    password_input_element = chrome_driver.find_element(By.XPATH, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    """Login_button"""
    login_button_locator = "//*[@id='login-button']"
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    error_locator = "//*[@data-test='error']"
    error_element = chrome_driver.find_element(By.XPATH, error_locator)
    error_message = "Epic sadface: Sorry, this user has been locked out."
    assert error_element.text == error_message, f"User cannot login the {error_message} is displayed"


def test_locked_user_error():
    """Pre_set_up"""
    user_name = "locked_out_user"
    password = "secret_sauce"
    chrome_driver = Chrome("Automation_tests/utilities/chromedriver")
    chrome_driver.get("https://www.saucedemo.com")
    """Email_input"""
    email_input_locator = "//input[@id='user-name']"
    email_input_element = chrome_driver.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_name)
    """Password_input"""
    password_input_locator = "//input[@id='password']"
    password_input_element = chrome_driver.find_element(By.XPATH, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    """Login_button"""
    login_button_locator = "//*[@id='login-button']"
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    chrome_driver.implicitly_wait(1)
    """Result"""
    error_locator = "//*[@data-test='error']"
    # error_locator = "//*[contains(text(),'Epic sadface: Sorry, this user has been locked out.')]"
    error_element = chrome_driver.find_element(By.XPATH, error_locator)
    assert error_element.text == "Epic sadface: Sorry, this user has been locked out."


def test_problem_user():
    """Pre_set_up"""
    user_name = "problem_user"
    password = "secret_sauce"
    chrome_driver = Chrome("Automation_tests/utilities/chromedriver")
    chrome_driver.get("https://www.saucedemo.com")
    """Email_input"""
    email_input_locator = "//input[@id='user-name']"
    email_input_element = chrome_driver.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_name)
    """Password_input"""
    password_input_locator = "//input[@id='password']"
    password_input_element = chrome_driver.find_element(By.XPATH, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    """Login_button"""
    login_button_locator = "//*[@id='login-button']"
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    actual_result = "https://www.saucedemo.com/inventory.html"
    assert actual_result == "https://www.saucedemo.com/inventory.html"


def test_performance_glitch_user():
    """Pre_set_up"""
    user_name = "performance_glitch_user"
    password = "secret_sauce"
    chrome_driver = Chrome("Automation_tests/utilities/chromedriver")
    chrome_driver.get("https://www.saucedemo.com")
    """Email_input"""
    email_input_locator = "//input[@id='user-name']"
    email_input_element = chrome_driver.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_name)
    """Password_input"""
    password_input_locator = "//input[@id='password']"
    password_input_element = chrome_driver.find_element(By.XPATH, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    """Login_button"""
    login_button_locator = "//*[@id='login-button']"
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    actual_result = "https://www.saucedemo.com/inventory.html"
    assert actual_result == "https://www.saucedemo.com/inventory.html"


def test_burger_menu():
    """Pre_set_up"""
    user_name = "standard_user"
    password = "secret_sauce"
    chrome_driver = Chrome("Automation_tests/utilities/chromedriver")
    chrome_driver.get("https://www.saucedemo.com")
    """Email_input"""
    email_input_locator = "//input[@id='user-name']"
    email_input_element = chrome_driver.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_name)
    """Password_input"""
    password_input_locator = "//input[@id='password']"
    password_input_element = chrome_driver.find_element(By.XPATH, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    """Login_button"""
    login_button_locator = "//*[@id='login-button']"
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    """Burger_menu"""
    burger_menu_locator = "//*[@id='react-burger-menu-btn']"
    burger_menu_element = chrome_driver.find_element(By.XPATH, burger_menu_locator)
    burger_menu_element.click()
    all_items_locator = "//*[@id='inventory_sidebar_link']"
    all_items_item = chrome_driver.find_element(By.XPATH, all_items_locator)
    about_locator = "//*[@id='about_sidebar_link']"
    about_item = chrome_driver.find_element(By.XPATH, about_locator)
    logout_locator = "//*[@id='logout_sidebar_link']"
    logout_item = chrome_driver.find_element(By.XPATH, logout_locator)
    reset_app_state_locator = "//*[@id='reset_sidebar_link']"
    reset_app_state_item = chrome_driver.find_element(By.XPATH, reset_app_state_locator)
    assert all_items_item.text == "ALL ITEMS"
    assert about_item.text == "ABOUT"
    assert logout_item.text == "LOGOUT"
    assert reset_app_state_item.text == "RESET APP STATE"


def test_about(create_driver, create_wait_object, ):
    chrome_driver = create_driver
    wait = create_wait_object
    """Email_input"""
    email_input_locator = "//input[@id='user-name']"
    email_input_element = chrome_driver.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(ReadConfig.get_standard_user_name())
    """Password_input"""
    password_input_locator = "//input[@id='password']"
    password_input_element = chrome_driver.find_element(By.XPATH, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(ReadConfig.get_password())
    """Login_button"""
    login_button_locator = "//*[@id='login-button']"
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    """Burger_menu"""
    burger_menu_locator = "//*[@id='react-burger-menu-btn']"
    burger_menu_element = chrome_driver.find_element(By.XPATH, burger_menu_locator)
    burger_menu_element.click()
    about_locator = "//*[@id='about_sidebar_link']"
    # about_element = chrome_driver.find_element(By.XPATH, about_locator)
    about_element = wait.until(EC.element_to_be_clickable((By.XPATH, about_locator)))
    # chrome_driver.implicitly_wait(5)
    about_element.click()
    actual_title = chrome_driver.title
    assert actual_title == "Cross Browser Testing, Selenium Testing, Mobile Testing | Sauce Labs"


def test_log_out():
    """Pre_set_up"""
    user_name = "standard_user"
    password = "secret_sauce"
    chrome_driver = Chrome("Automation_tests/utilities/chromedriver")
    chrome_driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(chrome_driver, 5)
    """Email_input"""
    email_input_locator = "//input[@id='user-name']"
    email_input_element = chrome_driver.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_name)
    """Password_input"""
    password_input_locator = "//input[@id='password']"
    password_input_element = chrome_driver.find_element(By.XPATH, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    """Login_button"""
    login_button_locator = "//*[@id='login-button']"
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    """Burger_menu"""
    burger_menu_locator = "//*[@id='react-burger-menu-btn']"
    burger_menu_element = chrome_driver.find_element(By.XPATH, burger_menu_locator)
    burger_menu_element.click()
    logout_locator = "//*[@id='logout_sidebar_link']"
    # logout_item = chrome_driver.find_element(By.XPATH, logout_locator)
    logout_item = wait.until(EC.element_to_be_clickable((By.XPATH, logout_locator)))
    # chrome_driver.implicitly_wait(5)
    logout_item.click()
    actual_title = chrome_driver.title
    assert actual_title == "Swag Labs"


def test_shopping_cart():
    """Pre_set_up"""
    user_name = "standard_user"
    password = "secret_sauce"
    chrome_driver = Chrome("Automation_tests/utilities/chromedriver")
    chrome_driver.get("https://www.saucedemo.com")
    """Email_input"""
    email_input_locator = "//input[@id='user-name']"
    email_input_element = chrome_driver.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_name)
    """Password_input"""
    password_input_locator = "//input[@id='password']"
    password_input_element = chrome_driver.find_element(By.XPATH, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    """Login_button"""
    login_button_locator = "//*[@id='login-button']"
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    """Shopping_cart"""
    shopping_cart_locator = "//*[@id='shopping_cart_container']"
    shopping_cart_item = chrome_driver.find_element(By.XPATH, shopping_cart_locator)
    shopping_cart_item.click()
    your_cart_locator = "//*[@id='header_container']//span"
    your_cart_item = chrome_driver.find_element(By.XPATH, your_cart_locator)
    assert your_cart_item.text == "YOUR CART"


def test_add_to_shopping_cart():
    """Pre_set_up"""
    user_name = "standard_user"
    password = "secret_sauce"
    chrome_driver = Chrome("Automation_tests/utilities/chromedriver")
    chrome_driver.get("https://www.saucedemo.com")
    """Email_input"""
    email_input_locator = "#user-name"
    email_input_element = chrome_driver.find_element(By.CSS_SELECTOR, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_name)
    """Password_input"""
    password_input_locator = "#password"
    password_input_element = chrome_driver.find_element(By.CSS_SELECTOR, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    """Login_button"""
    login_button_locator = "#login-button"
    login_button_element = chrome_driver.find_element(By.CSS_SELECTOR, login_button_locator)
    login_button_element.click()
    """Add_to_cart"""
    add_to_cart_button_locator = "#add-to-cart-sauce-labs-backpack"
    add_to_cart_button_item = chrome_driver.find_element(By.CSS_SELECTOR, add_to_cart_button_locator)
    add_to_cart_button_item.click()
    """Shopping_cart"""
    shopping_cart_locator = "#shopping_cart_container"
    shopping_cart_item = chrome_driver.find_element(By.CSS_SELECTOR, shopping_cart_locator)
    shopping_cart_item.click()
    item_in_shopping_cart_locator = "#item_4_title_link"
    item_in_shopping_cart_item = chrome_driver.find_element(By.CSS_SELECTOR, item_in_shopping_cart_locator)
    expected_result = "Sauce Labs Backpack"
    assert item_in_shopping_cart_item.text == expected_result


def test_checkout():
    """Pre_set_up"""
    user_name = "standard_user"
    password = "secret_sauce"
    chrome_driver = Chrome("Automation_tests/utilities/chromedriver")
    chrome_driver.get("https://www.saucedemo.com")
    """Email_input"""
    email_input_locator = "#user-name"
    email_input_element = chrome_driver.find_element(By.CSS_SELECTOR, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_name)
    """Password_input"""
    password_input_locator = "#password"
    password_input_element = chrome_driver.find_element(By.CSS_SELECTOR, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    """Login_button"""
    login_button_locator = "#login-button"
    login_button_element = chrome_driver.find_element(By.CSS_SELECTOR, login_button_locator)
    login_button_element.click()
    """Add_to_cart"""
    add_to_cart_button_locator = "#add-to-cart-sauce-labs-backpack"
    add_to_cart_button_item = chrome_driver.find_element(By.CSS_SELECTOR, add_to_cart_button_locator)
    add_to_cart_button_item.click()
    """Shopping_cart"""
    shopping_cart_locator = "#shopping_cart_container"
    shopping_cart_item = chrome_driver.find_element(By.CSS_SELECTOR, shopping_cart_locator)
    shopping_cart_item.click()
    """Checkout"""
    checkout_button_locator = "#checkout"
    checkout_button_item = chrome_driver.find_element(By.CSS_SELECTOR, checkout_button_locator)
    checkout_button_item.click()
    """Checkout_information"""
    first_name = "Oleksii"
    last_name = "Fedorchuk"
    postal_code = 61001
    """First_name_field"""
    first_name_locator = "#first-name"
    first_name_item = chrome_driver.find_element(By.CSS_SELECTOR, first_name_locator)
    first_name_item.send_keys(first_name)
    """Last_name_field"""
    last_name_locator = "#last-name"
    last_name_item = chrome_driver.find_element(By.CSS_SELECTOR, last_name_locator)
    last_name_item.send_keys(last_name)
    """Postal_code_field"""
    postal_code_locator = "#postal-code"
    postal_code_item = chrome_driver.find_element(By.CSS_SELECTOR, postal_code_locator)
    postal_code_item.send_keys(postal_code)
    continue_button_locator = "//*[@id='continue']"
    continue_button_item = chrome_driver.find_element(By.XPATH, continue_button_locator)
    continue_button_item.click()
    """Checkout_overview"""
    inventory_item_locator = "//*[@id='item_4_title_link']/div"
    inventory_item = chrome_driver.find_element(By.XPATH, inventory_item_locator)
    assert inventory_item.text == "Sauce Labs Backpack"
    finish_button_locator = "//*[@id='finish']"
    finish_button_item = chrome_driver.find_element(By.XPATH, finish_button_locator)
    finish_button_item.click()
    complete_header_locator = "//*[@id='checkout_complete_container']/h2"
    complete_header_item = chrome_driver.find_element(By.XPATH, complete_header_locator)
    assert complete_header_item.text == "THANK YOU FOR YOUR ORDER"


def test_remove_from_shopping_cart():
    """Pre_set_up"""
    user_name = "standard_user"
    password = "secret_sauce"
    chrome_driver = Chrome("Automation_tests/utilities/chromedriver")
    chrome_driver.get("https://www.saucedemo.com")
    """Email_input"""
    email_input_locator = "//input[@id='user-name']"
    email_input_element = chrome_driver.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_name)
    """Password_input"""
    password_input_locator = "//input[@id='password']"
    password_input_element = chrome_driver.find_element(By.XPATH, password_input_locator)
    password_input_element.clear()
    password_input_element.send_keys(password)
    """Login_button"""
    login_button_locator = "//*[@id='login-button']"
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    """Add_to_cart"""
    add_to_cart_button_locator = "//*[@id='add-to-cart-sauce-labs-backpack']"
    add_to_cart_button_item = chrome_driver.find_element(By.XPATH, add_to_cart_button_locator)
    add_to_cart_button_item.click()
    """Shopping_cart"""
    shopping_cart_locator = "//*[@id='shopping_cart_container']"
    shopping_cart_item = chrome_driver.find_element(By.XPATH, shopping_cart_locator)
    shopping_cart_item.click()
    item_in_shopping_cart_locator = "//*[@id='item_4_title_link']"
    item_in_shopping_cart_item = chrome_driver.find_element(By.XPATH, item_in_shopping_cart_locator)
    """Remove_from_cart"""
    remove_item_fom_shopping_cart_locator = "//*[@id='remove-sauce-labs-backpack']"
    remove_item_fom_shopping_cart_item = chrome_driver.find_element(By.XPATH, remove_item_fom_shopping_cart_locator)
    remove_item_fom_shopping_cart_item.click()
    assert item_in_shopping_cart_item is not True
