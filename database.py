from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()


class Database:
    def __init__(self):
        self._hostname = os.getenv("DB_HOSTNAME")
        self._user = os.getenv("DB_USERNAME")
        self._password = os.getenv("DB_PASSWORD")
        self._connection = mysql.connector.connect(host=self._hostname, user=self._user, password=self._password)
        self._cursor = self._connection.cursor(dictionary=True)

    def execute(self, query):
        self._cursor.execute(query)
        return self._cursor.fetchall()

    def select_all(self, table_name: str) -> list:
        self._cursor.execute(f"SELECT * FROM test_db.{table_name}")
        return self._cursor.fetchall()

    def select(self, columns: list, table_name: str) -> list:
        self._cursor.execute(f"SELECT {', '.join(columns)} FROM test_db.{table_name}")
        return self._cursor.fetchall()

    def insert(self, columns: list, values: list, table_name: str) -> str:
        query = f"INSERT INTO test_db.{table_name} ({', '.join(columns)}) VALUES ('{values[0]}', {values[1]})"
        print(query)
        try:
            return self._cursor.execute(query)
        except mysql.connector.errors.ProgrammingError as e:
            return e
