import sqlite3
from sqlite3 import Error

cursorObj = type(sqlite3.connect('').cursor())


def db_connect(func):
    def decorator(*args):
        try:
            db = sqlite3.connect('data.db')
            cur = db.cursor()
            func(cur, *args)
            db.commit()
            db.close()
        except Error:
            print(Error)

    return decorator


@db_connect
def create_db(cur: cursorObj):
    cur.execute("CREATE TABLE IF NOT EXISTS users(user_id integer PRIMARY KEY, name text)")
    cur.execute("""CREATE TABLE IF NOT EXISTS teams(team_id integer PRIMARY KEY, leader_id integer, 
    member_1_id integer, member_2_id integer, member_3_id integer, member_4_id integer, member_5_id integer, 
    member_6_id integer, member_7_id integer, member_8_id integer)""")


@db_connect
def user_check(cur: cursorObj, user_id):
    cur.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
    info = cur.fetchall() is None
    return info


