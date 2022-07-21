import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('data.db')
        return con
    except Error:
        print(Error)


def create_table_users(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE users(telegram_id integer PRIMARY KEY, name text, )")


def worker():
    connection = sql_connection()
    create_table_users(connection)

