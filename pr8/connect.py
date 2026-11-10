import psycopg2
from config import DB_CONFIG


def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = True  # процедуры сами управляют транзакциями
    return conn


def run_sql_file(conn, path):
    """Выполнить .sql файл (создать функции / процедуры)."""
    with open(path, encoding="utf-8") as f, conn.cursor() as cur:
        cur.execute(f.read())
