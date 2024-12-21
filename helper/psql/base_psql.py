import psycopg2
from psycopg2.extras import RealDictCursor

def check_func(func):
    def wrapper_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(error)

    return wrapper_func



class BasePSQL:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="kino_bot",
            password="postgres",
            host="localhost",
            user="postgres",
            port=5432,
            cursor_factory=RealDictCursor,
            # [RealDictCursor] it helps to get data on json objects
        )

        self.cur = self.conn.cursor()

    @check_func
    def close_connection(self):
        self.cur.close()
        self.conn.close()