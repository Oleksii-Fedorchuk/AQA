import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_title():
    """Pre_set_up"""
    chrome_driver = Chrome("Automation_tests/utilities/chromedriver")
    chrome_driver.maximize_window()
    chrome_driver.get("https://www.saucedemo.com")
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
    time.sleep(1)
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


def test_about():
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
    about_locator = "//*[@id='about_sidebar_link']"
    about_locator = chrome_driver.find_element(By.XPATH, about_locator)
    time.sleep(0.5)
    about_locator.click()
    actual_title = chrome_driver.title
    assert actual_title == "Cross Browser Testing, Selenium Testing, Mobile Testing | Sauce Labs"


def test_log_out():
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
    logout_locator = "//*[@id='logout_sidebar_link']"
    logout_item = chrome_driver.find_element(By.XPATH, logout_locator)
    time.sleep(0.5)
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
    expected_result = "Sauce Labs Backpack"
    assert item_in_shopping_cart_item.text == expected_result


def test_checkout():
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
    """Checkout"""
    checkout_button_locator = "//*[@id='checkout']"
    checkout_button_item = chrome_driver.find_element(By.XPATH, checkout_button_locator)
    checkout_button_item.click()
    """Checkout_information"""
    first_name = "Oleksii"
    last_name = "Fedorchuk"
    postal_code = 61001
    """First_name_field"""
    first_name_locator = "//input[@id='first-name']"
    first_name_item = chrome_driver.find_element(By.XPATH, first_name_locator)
    first_name_item.send_keys(first_name)
    """Last_name_field"""
    last_name_locator = "//input[@id='last-name']"
    last_name_item = chrome_driver.find_element(By.XPATH, last_name_locator)
    last_name_item.send_keys(last_name)
    """Postal_code_field"""
    postal_code_locator = "//input[@id='postal-code']"
    postal_code_item = chrome_driver.find_element(By.XPATH, postal_code_locator)
    postal_code_item.send_keys(postal_code)
    continue_button_locator = "//*[@id='continue']"
    continue_button_item = chrome_driver.find_element(By.XPATH, continue_button_locator)
    continue_button_item.click()
    """Order_information"""
    item_total_cost_locator = "//*[@id='checkout_summary_container']/div/div[2]/div[5]/text()[2]"
    item_total_cost_item = chrome_driver.find_element(By.XPATH, item_total_cost_locator)
    taxes_locator = "//*[@id='checkout_summary_container']/div/div[2]/div[6]/text()[2]]"
    taxes_item = chrome_driver.find_element(By.XPATH, taxes_locator)
    total_sum_locator = "//*[@id='checkout_summary_container']/div/div[2]/div[7]/text()[2]]"
    total_sum_item = chrome_driver.find_element(By.XPATH, total_sum_locator)
    assert total_sum_item == int(item_total_cost_item) + int(taxes_item)


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
