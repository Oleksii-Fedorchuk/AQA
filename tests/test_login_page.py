import pytest
from CONSTANTS import locked_error_on_login_page
from utilities.config_parser import ReadConfig


def test_title(open_login_page):
    assert open_login_page.current_title() == open_login_page.title_name


# @pytest.mark.parametrize("user", (
#         ReadConfig.get_standard_user_name(), ReadConfig.get_problem_user_name(),
#         ReadConfig.get_performance_glitch_user_name()))
# def test_login_as_valid_users(open_login_page, user):
#     open_login_page.login(user)
#     assert open_login_page.current_url() == open_login_page.inventory_page_url


def test_login_as_invalid_users(open_login_page, env):
    # open_login_page.login(ReadConfig.get_locked_user_name()) # from Readconfig
    open_login_page.login(env.locked_user_name)
    assert open_login_page._is_login_error_text() == locked_error_on_login_page


def test_logout(open_login_page, burger_menu, env):
    # open_login_page.login(ReadConfig.get_standard_user_name()) # from Readconfig
    open_login_page.login(env.standard_user_name)
    burger_menu.open_burger_menu()
    burger_menu.click_logout_button()
    assert open_login_page.current_url() == open_login_page.login_page_url


