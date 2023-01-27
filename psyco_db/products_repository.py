from Automation_tests.psyco_db.base_repository import BaseRepository


class ProductsRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self._table_name = "products"

    def get_product_name(self):
        self._cursor.execute("Select name from products")
        return self._cursor.fetchall()

    def get_price_by_product_name(self, name: str):
        self._cursor.execute(f"Select * from products where products.name = '{name}'")
        return self._cursor.fetchone()

    def get_list_of_products_name_and_price(self):
        self._cursor.execute("Select name, price from products")
        return self._cursor.fetchall()

    def insert_product(self, product_id: int, name: str, price: int):
        self._cursor.execute(f"insert into products (id, name, price) values ({product_id}, '{name}', {price});")

    def delete_user_by_name(self, name: str):
        self._cursor.execute(f"delete from products where products.name = '{name}'")

    def __del__(self):
        if self._connection:
            if self._cursor:
                self._cursor.close()
            self._connection.close()
