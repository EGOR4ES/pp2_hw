import psycopg2
from config import DB_CONFIG


def get_connection():
    """Open and return a new PostgreSQL connection."""
    try:
        return psycopg2.connect(**DB_CONFIG)
    except psycopg2.OperationalError as e:
        print(f"Could not connect to the database: {e}")
        raise


if __name__ == "__main__":
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("SELECT version();")
        print(cur.fetchone()[0])
    conn.close()
