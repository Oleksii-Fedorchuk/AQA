from Automation_tests.psyco_db.products_repository import ProductsRepository

products_repository = ProductsRepository()


def test_get_all_products():
    products = products_repository.get_all()
    assert products


def test_get_product_price_by_name():
    product_price = products_repository.get_price_by_product_name('Iphone')
    expected = 1000
    assert product_price[2] == expected


def test_get_list_of_products_name_and_price():
    list_of_name_and_price = products_repository.get_list_of_products_name_and_price()
    assert list_of_name_and_price


def test_insert_product():
    products_repository.insert_product(6, "MacBookPro 2023", 1999)
    products = products_repository.get_all()
    expected = (6, "MacBookPro 2023", 1999)
    for product in products:
        if product == (6, "MacBookPro 2023", 1999):
            assert product == expected


def test_delete_from_products_by_name():
    products_repository.delete_user_by_name("MacBookPro 2023")
    products = products_repository.get_all()
    expected = "MacBookPro 2023"
    for product in products:
        assert product is not expected
