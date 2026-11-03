import csv
import psycopg2
from connect import get_connection

CSV_FILE = "contacts.csv"


# ---------- 1. Table design ----------
def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS contacts (
        id         SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        phone      VARCHAR(20) NOT NULL UNIQUE
    );
    """
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:   # `with conn` commits / rolls back
            cur.execute(sql)
        print("Table 'contacts' is ready.")
    finally:
        conn.close()


# ---------- 2. Insert from CSV ----------
def insert_from_csv(path=CSV_FILE):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            rows = [(r["first_name"].strip(), r["phone"].strip())
                    for r in csv.DictReader(f)]
    except FileNotFoundError:
        print(f"File not found: {path}")
        return

    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.executemany(
                "INSERT INTO contacts (first_name, phone) VALUES (%s, %s) "
                "ON CONFLICT (phone) DO NOTHING;",
                rows,
            )
        print(f"Processed {len(rows)} rows from {path} (duplicates skipped).")
    finally:
        conn.close()


# ---------- 3. Insert from console ----------
def insert_from_console():
    name = input("First name: ").strip()
    phone = input("Phone: ").strip()
    if not name or not phone:
        print("Name and phone cannot be empty.")
        return

    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO contacts (first_name, phone) VALUES (%s, %s);",
                (name, phone),
            )
        print("Contact added.")
    except psycopg2.errors.UniqueViolation:
        print("A contact with this phone number already exists.")
    finally:
        conn.close()


# ---------- 4. Update ----------
def update_contact():
    old_phone = input("Phone of the contact to update: ").strip()
    choice = input("Update (1) first name or (2) phone? ").strip()

    if choice == "1":
        column, value = "first_name", input("New first name: ").strip()
    elif choice == "2":
        column, value = "phone", input("New phone: ").strip()
    else:
        print("Invalid choice.")
        return

    # column comes from a fixed set above, never from user text
    sql = f"UPDATE contacts SET {column} = %s WHERE phone = %s;"
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(sql, (value, old_phone))
            print(f"Updated {cur.rowcount} contact(s).")
    except psycopg2.errors.UniqueViolation:
        print("That phone number is already used by another contact.")
    finally:
        conn.close()


# ---------- 5. Query with filters ----------
def query_contacts():
    print("Filter by: 1) all  2) name  3) phone prefix")
    choice = input("Choice: ").strip()

    if choice == "1":
        sql, params = "SELECT id, first_name, phone FROM contacts ORDER BY first_name;", ()
    elif choice == "2":
        name = input("Name (partial ok): ").strip()
        sql = ("SELECT id, first_name, phone FROM contacts "
               "WHERE first_name ILIKE %s ORDER BY first_name;")
        params = (f"%{name}%",)
    elif choice == "3":
        prefix = input("Phone prefix: ").strip()
        sql = ("SELECT id, first_name, phone FROM contacts "
               "WHERE phone LIKE %s ORDER BY first_name;")
        params = (f"{prefix}%",)
    else:
        print("Invalid choice.")
        return

    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()
        if not rows:
            print("No contacts found.")
        for r in rows:
            print(f"{r[0]:>3} | {r[1]:<20} | {r[2]}")
    finally:
        conn.close()


# ---------- 6. Delete ----------
def delete_contact():
    choice = input("Delete by (1) username or (2) phone? ").strip()
    if choice == "1":
        sql, value = "DELETE FROM contacts WHERE first_name = %s;", input("Username: ").strip()
    elif choice == "2":
        sql, value = "DELETE FROM contacts WHERE phone = %s;", input("Phone: ").strip()
    else:
        print("Invalid choice.")
        return

    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(sql, (value,))
            print(f"Deleted {cur.rowcount} contact(s).")
    finally:
        conn.close()


# ---------- Menu ----------
def main():
    create_table()
    actions = {
        "1": ("Import from CSV", insert_from_csv),
        "2": ("Add contact (console)", insert_from_console),
        "3": ("Update contact", update_contact),
        "4": ("Query contacts", query_contacts),
        "5": ("Delete contact", delete_contact),
    }
    while True:
        print("\n=== PhoneBook ===")
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")
        print("0. Exit")
        choice = input("Choice: ").strip()
        if choice == "0":
            break
        if choice in actions:
            try:
                actions[choice][1]()
            except psycopg2.Error as e:
                print(f"Database error: {e}")
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
