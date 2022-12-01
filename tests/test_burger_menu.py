from Automation_tests.utilities.config_parser import ReadConfig


def test_burger_menu(open_login_page, open_burger_menu):
    open_login_page.set_email(ReadConfig.get_standard_user_name()).set_password(
        ReadConfig.get_password()).click_login_button()
    open_burger_menu.get_burger_menu()
    assert open_burger_menu.read_text(open_burger_menu.get_all_items()) == "ALL ITEMS"
    assert open_burger_menu.read_text(open_burger_menu.get_about()) == "ABOUT"
    assert open_burger_menu.read_text(open_burger_menu.get_logout()) == "LOGOUT"
    assert open_burger_menu.read_text(open_burger_menu.get_reset_app_state()) == "RESET APP STATE"


def test_about(open_login_page, open_burger_menu, create_driver):
    open_login_page.set_email(ReadConfig.get_standard_user_name()).set_password(
        ReadConfig.get_password()).click_login_button()
    open_burger_menu.get_burger_menu()
    open_burger_menu.click_on(open_burger_menu.get_about())
    assert create_driver.current_url == open_burger_menu.about_url()
