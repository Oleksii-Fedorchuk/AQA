import pymongo


class BaseRepository:
    def __init__(self, database, collection):
        self._connection = pymongo.MongoClient("mongodb://localhost:27017/")
        self._database = self._connection[database]
        self._collection = self._database[collection]

    def insert_data(self, data_to_add: dict):
        self._collection.insert_one(data_to_add)

    def find_one(self, data_to_find: dict):
        find_one = self._collection.find_one(data_to_find)
        return find_one

    def find(self, data_to_find):
        find = self._collection.find(data_to_find)
        return find

    def delete_one(self, data_to_delete: dict):
        self._collection.delete_one(data_to_delete)

# client = pymongo.MongoClient("mongodb://localhost:27017/")
# products_db = client["products"]
# my_collection = products_db["new_products"]
# data_to_add = {"key1": "value1"}
# datas_to_add = [{"key2": "value2"}, {"key3": "value3"}]
# inserted_obj = my_collection.insert_one(data_to_add)
# # print(inserted_obj.inserted_id)
# result = my_collection.insert_many(datas_to_add)
# print(result.inserted_ids)
