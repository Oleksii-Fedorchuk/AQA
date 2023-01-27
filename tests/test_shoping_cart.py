# from Automation_tests.utilities.config_parser import ReadConfig


def test_shopping_cart(open_login_page, shopping_cart, env):
    # open_login_page.login(ReadConfig.get_standard_user_name()) # from Readconfig
    open_login_page.login(env.standard_user_name)
    shopping_cart.open_shopping_cart()
    assert shopping_cart.your_cart() == shopping_cart.your_cart_text()


def test_add_to_shopping_cart(open_login_page, shopping_cart, env):
    # open_login_page.login(ReadConfig.get_standard_user_name()) # from Readconfig
    open_login_page.login(env.standard_user_name)
    shopping_cart.click_on_add_to_cart_button()
    shopping_cart.open_shopping_cart()
    assert shopping_cart.item_in_shopping_cart() == shopping_cart.name_of_item_in_shopping_item()


def test_checkout(open_login_page, shopping_cart, env):
    # open_login_page.login(ReadConfig.get_standard_user_name()) # from Readconfig
    open_login_page.login(env.standard_user_name)
    shopping_cart.click_on_add_to_cart_button()
    shopping_cart.open_shopping_cart()
    shopping_cart.click_on_checkout_button()
    # shopping_cart.set_credentials(ReadConfig.get_client_first_name(), ReadConfig.get_client_last_name(),
    #                               ReadConfig.get_client_postal_code()) # from Readconfig
    shopping_cart.set_credentials(env.client_name, env.client_last_name,
                                  env.client_postal_code)
    shopping_cart.click_on_continue_button()
    assert shopping_cart.item_in_shopping_cart() == shopping_cart.name_of_item_in_shopping_item()
    shopping_cart.click_on_finish_button()
    assert shopping_cart.complete_header() == shopping_cart.complete_header_text()


def test_remove_from_shopping_cart(open_login_page, shopping_cart, env):
    # open_login_page.login(ReadConfig.get_standard_user_name()) # from Readconfig
    open_login_page.login(env.standard_user_name)
    shopping_cart.click_on_add_to_cart_button()
    shopping_cart.open_shopping_cart()
    shopping_cart.click_on_remove_from_shopping_cart_button()
    assert shopping_cart.item_in_shopping_cart is not True
