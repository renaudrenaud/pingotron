"""
Horrible Class for Postgres database connection and query execution

RC 2020-12-01
V0.1: it works


"""


import psycopg2
import psycopg2.extras

class Postgres:
    
    def __init__(self, host, port, db, user, password):
        self.__version__ = '0.1'
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password

    def connect(self):
        try:
            self.conn = psycopg2.connect(host=self.host, port=self.port, database=self.db, user=self.user, password=self.password)
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            return self.cur
        except Exception as e:
            print(e)

    def execute(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
            return self.cur
        except Exception as e:
            print(e)

    def close(self):
        self.cur.close()
        self.conn.close()