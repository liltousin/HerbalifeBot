import sqlite3
from sqlite3 import Error


class Data:
    def __init__(self):
        def create_table_users(con):
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS users(telegram_id integer PRIMARY KEY, name text)")
            con.commit()

        def create_table_teams(con):
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS teams(team_id integer PRIMARY KEY, leader_id integer, 
            member_1_id integer, member_2_id integer, member_3_id integer, member_4_id integer, member_5_id integer, 
            member_6_id integer, member_7_id integer, member_8_id integer)""")
            con.commit()

        try:
            self.con = sqlite3.connect('data.db')
            create_table_users(self.con)
            create_table_teams(self.con)
        except Error:
            print(Error)
        finally:
            self.con.close()

    def connect(self):
        self.con = sqlite3.connect('data.db')
        return self.con

    def close(self):
        self.con.close()
        return self.con
