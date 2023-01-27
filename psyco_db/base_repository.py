import psycopg2


class BaseRepository:
    def __init__(self):
        self._connection = psycopg2.connect(user="postgres",
                                            password="123",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="mydb")
        self._connection.set_session(autocommit=True)
        self._cursor = self._connection.cursor()
        self._table_name = ""

    def get_all(self):
        self._cursor.execute(f"Select * from {self._table_name}")
        return self._cursor.fetchall()

    def delete_user_by_name(self, name):
        self._cursor.execute(f"delete from products where products.name = '{name}';")
