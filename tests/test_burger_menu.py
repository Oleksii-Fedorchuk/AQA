from Automation_tests.utilities.config_parser import ReadConfig
from CONSTANTS import burger_nemu_list


def test_burger_menu(open_login_page, burger_menu):
    open_login_page.login(ReadConfig.get_standard_user_name())
    burger_menu.open_burger_menu()
    assert burger_menu.list_of_burger_menu() == burger_nemu_list


def test_about(open_login_page, burger_menu):
    open_login_page.login(ReadConfig.get_standard_user_name())
    burger_menu.open_burger_menu()
    burger_menu.click_on_about()
    assert burger_menu.current_url() == burger_menu.about_url
