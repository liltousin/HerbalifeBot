import sqlite3
from sqlite3 import Error


class Data:
    def __init__(self):
        try:
            self.con = sqlite3.connect('data.db')
        except Error:
            print(Error)

    def create_table_users(self):
        cur = self.con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users(telegram_id integer PRIMARY KEY, name text)")
        self.con.commit()

    def create_table_teams(self):
        cur = self.con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS teams(team_id integer PRIMARY KEY, leader_id integer, member_1_id integer, 
        member_2_id integer, member_3_id integer, member_4_id integer, member_5_id integer, member_6_id integer, 
        member_7_id integer, member_8_id integer)""")
        self.con.commit()


def worker():
    data = Data()
    data.create_table_teams()
    data.create_table_users()