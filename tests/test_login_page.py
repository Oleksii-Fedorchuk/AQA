from Automation_tests.utilities.config_parser import ReadConfig


def test_title(open_login_page, create_driver):
    assert create_driver.title == open_login_page.get_title()


def test_login_as_standard_user(open_login_page):
    open_login_page.set_email(ReadConfig.get_standard_user_name()).set_password(
        ReadConfig.get_password()).click_login_button()


def test_login_as_locked_user(open_login_page):
    open_login_page.set_email(ReadConfig.get_locked_user_name()).set_password(
        ReadConfig.get_password()).click_login_button()
    assert open_login_page.get_text() == open_login_page.get_locked_error()


def test_login_as_problem_user(open_login_page, dashboard_page):
    open_login_page.set_email(ReadConfig.get_problem_user_name()).set_password(
        ReadConfig.get_password()).click_login_button()
    assert dashboard_page.get_invalid_image()


def test_login_performance_glitch_user(open_login_page, inventory_page):
    open_login_page.set_email(ReadConfig.get_performance_glitch_user_name()).set_password(
        ReadConfig.get_password()).click_login_button()
    assert inventory_page.get_inventory_url


def test_logout(open_login_page, open_burger_menu, create_driver):
    open_login_page.set_email(ReadConfig.get_standard_user_name()).set_password(
        ReadConfig.get_password()).click_login_button()
    open_burger_menu.get_burger_menu()
    open_burger_menu.click_on(open_burger_menu.get_logout())
    assert create_driver.current_url == open_login_page.login_page_url()
