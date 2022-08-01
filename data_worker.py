import sqlite3
from sqlite3 import Error


class Data:
    def __init__(self):
        try:
            self.db = sqlite3.connect('data.db')
            cur = self.db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS users(user_id integer PRIMARY KEY, name text)")
            cur.execute("""CREATE TABLE IF NOT EXISTS teams(team_id integer PRIMARY KEY, leader_id integer, 
            member_1_id integer, member_2_id integer, member_3_id integer, member_4_id integer, member_5_id integer, 
            member_6_id integer, member_7_id integer, member_8_id integer)""")
            self.db.commit()
        except Error:
            print(Error)
        finally:
            self.db.close()

    def user_check(self, user_id):
        try:
            self.db = sqlite3.connect('data.db')
            cur = self.db.cursor()
            info = cur.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
        except Error:
            print(Error)
        finally:
            self.db.close()


