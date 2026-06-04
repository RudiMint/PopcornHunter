import pymysql

from contextlib import contextmanager

from utils.configuration import config


@contextmanager
def get_connection():
    """
    Context manager for creating and safely closing a MySQL database connection.
    :yields: Active MySQL database connection.
    Example:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
    """
    conn = pymysql.connect(**config)
    try:
        yield conn
    finally:
        conn.close()