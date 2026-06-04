import pymysql

from contextlib import contextmanager

from utils.configuration import config


@contextmanager
def get_connection():
    conn = pymysql.connect(**config)
    try:
        yield conn
    finally:
        conn.close()