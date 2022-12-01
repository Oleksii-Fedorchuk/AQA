from Automation_tests.utilities.config_parser import ReadConfig


def test_shopping_cart(open_login_page, shopping_cart):
    open_login_page.set_email(ReadConfig.get_standard_user_name()).set_password(
        ReadConfig.get_password()).click_login_button()
    shopping_cart.click_on(shopping_cart.get_shopping_cart())
    assert shopping_cart.read_text(shopping_cart.your_cart()) == shopping_cart.your_cart_text()


def test_add_to_shopping_cart(open_login_page, shopping_cart):
    open_login_page.set_email(ReadConfig.get_standard_user_name()).set_password(
        ReadConfig.get_password()).click_login_button()
    shopping_cart.click_on(shopping_cart.add_to_cart_button())
    shopping_cart.click_on(shopping_cart.get_shopping_cart())
    assert shopping_cart.get_text(
        shopping_cart.item_in_shopping_cart()) == shopping_cart.name_of_item_in_shopping_item()


def test_checkout(open_login_page, shopping_cart):
    open_login_page.set_email(ReadConfig.get_standard_user_name()).set_password(
        ReadConfig.get_password()).click_login_button()
    shopping_cart.click_on(shopping_cart.add_to_cart_button())
    shopping_cart.click_on(shopping_cart.get_shopping_cart())
    shopping_cart.click_on(shopping_cart.checkout_button())
    shopping_cart.set_first_name(ReadConfig.get_client_first_name())
    shopping_cart.set_last_name(ReadConfig.get_client_last_name())
    shopping_cart.set_postal_code_input(ReadConfig.get_client_postal_code())
    shopping_cart.click_on(shopping_cart.continue_button())
    assert shopping_cart.get_text(
        shopping_cart.item_in_shopping_cart()) == shopping_cart.name_of_item_in_shopping_item()
    shopping_cart.click_on(shopping_cart.finish_button())
    assert shopping_cart.read_text(shopping_cart.complete_header()) == shopping_cart.complete_header_text()


def test_remove_from_shopping_cart(open_login_page, shopping_cart):
    open_login_page.set_email(ReadConfig.get_standard_user_name()).set_password(
        ReadConfig.get_password()).click_login_button()
    shopping_cart.click_on(shopping_cart.add_to_cart_button())
    shopping_cart.click_on(shopping_cart.get_shopping_cart())
    shopping_cart.click_on(shopping_cart.remove_from_shopping_cart_button())
    assert shopping_cart.item_in_shopping_cart() is not True
