from connect import get_connection, run_sql_file


def init_db(conn):
    run_sql_file(conn, "functions.sql")
    run_sql_file(conn, "procedures.sql")
    print("Functions and procedures created.")


def search(conn):
    pattern = input("Pattern (name or phone part): ")
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
        for row in cur.fetchall():
            print(row)


def upsert(conn):
    name = input("Name: ")
    phone = input("Phone: ")
    with conn.cursor() as cur:
        cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    print("Done.")


def bulk_insert(conn):
    names, phones = [], []
    print("Enter 'name phone' per line, empty line to finish:")
    while True:
        line = input("> ").strip()
        if not line:
            break
        name, _, phone = line.rpartition(" ")
        names.append(name)
        phones.append(phone)
    with conn.cursor() as cur:
        cur.execute(
            "CALL insert_many_contacts(%s::varchar[], %s::varchar[], NULL::text[])",
            (names, phones),
        )
        invalid = cur.fetchone()[0]
    print("Incorrect data:", invalid if invalid else "none")


def paginate(conn):
    limit = int(input("Page size: "))
    page = 0
    while True:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, page * limit))
            rows = cur.fetchall()
        if not rows:
            print("(no more rows)")
            page = max(page - 1, 0)
        for row in rows:
            print(row)
        cmd = input("[n]ext / [p]rev / [q]uit: ").lower()
        if cmd == "n":
            page += 1
        elif cmd == "p":
            page = max(page - 1, 0)
        else:
            break


def delete(conn):
    value = input("Name or phone to delete: ")
    with conn.cursor() as cur:
        cur.execute("CALL delete_contact(%s)", (value,))
    print("Done.")


MENU = {
    "0": ("Init DB (create functions/procedures)", init_db),
    "1": ("Search by pattern", search),
    "2": ("Insert / update one contact", upsert),
    "3": ("Bulk insert with validation", bulk_insert),
    "4": ("Paginated view", paginate),
    "5": ("Delete by name or phone", delete),
}


def main():
    conn = get_connection()
    try:
        while True:
            print()
            for k, (title, _) in MENU.items():
                print(f"{k}. {title}")
            print("q. Quit")
            choice = input("Choice: ").strip().lower()
            if choice == "q":
                break
            if choice in MENU:
                try:
                    MENU[choice][1](conn)
                except Exception as e:
                    print("Error:", e)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
