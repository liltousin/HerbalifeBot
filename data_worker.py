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
    cur.execute("CREATE TABLE IF NOT EXISTS users(telegram_id integer PRIMARY KEY, name text)")
    con.commit()


def create_table_teams(con):
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS teams(team_id integer PRIMARY KEY, leader_id integer, member_1_id integer, 
    member_2_id integer, member_3_id integer, member_4_id integer, member_5_id integer, member_6_id integer, 
    member_7_id integer, member_8_id integer)""")
    con.commit()


def worker():
    connection = sql_connection()
    create_table_users(connection)
    create_table_teams(connection)
