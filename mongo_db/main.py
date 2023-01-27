from mongo_db.base_page import BaseRepository


class ProductsCollection(BaseRepository):
    def __init__(self):
        super().__init__("products", "product_collection")

    def find_by_amount(self, data_to_find):
        find_by_amount = self.find(data_to_find)
        return find_by_amount
