import csv
import psycopg2


def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="pp2_db",
        user="postgres",
        password="qwerty12345"
    )
    return conn


def create_table(): 
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20) UNIQUE
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created successfully.")


def insert_from_csv():
    conn = connect_db()
    cur = conn.cursor()

    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            name = row[0]
            phone = row[1]

            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
                (name, phone)
            )

    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted from CSV.")


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added.")


def update_contact():
    old_name = input("Enter contact name to update: ")
    print("1 - Update name")
    print("2 - Update phone")
    choice = input("Choose: ")

    conn = connect_db()
    cur = conn.cursor()

    if choice == "1":
        new_name = input("Enter new name: ")
        cur.execute(
            "UPDATE phonebook SET name = %s WHERE name = %s",
            (new_name, old_name)
        )
        print("Name updated.")
    elif choice == "2":
        new_phone = input("Enter new phone: ")
        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE name = %s",
            (new_phone, old_name)
        )
        print("Phone updated.")
    else:
        print("Wrong choice.")

    conn.commit()
    cur.close()
    conn.close()


def show_all_contacts():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    if len(rows) == 0:
        print("No contacts found.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()


def search_by_name():
    name = input("Enter name: ")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s",
        ('%' + name + '%',)
    )

    rows = cur.fetchall()

    if len(rows) == 0:
        print("No contacts found.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()


def search_by_phone():
    prefix = input("Enter phone prefix: ")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
        (prefix + '%',)
    )

    rows = cur.fetchall()

    if len(rows) == 0:
        print("No contacts found.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()


def delete_by_name():
    name = input("Enter name to delete: ")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()

    print("Deleted rows:", cur.rowcount)

    cur.close()
    conn.close()


def delete_by_phone():
    phone = input("Enter phone to delete: ")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()

    print("Deleted rows:", cur.rowcount)

    cur.close()
    conn.close()


while True:
    print("\nPHONEBOOK MENU")
    print("1. Create table")
    print("2. Insert from CSV")
    print("3. Insert from console")
    print("4. Update contact")
    print("5. Show all contacts")
    print("6. Search by name")
    print("7. Search by phone prefix")
    print("8. Delete by name")
    print("9. Delete by phone")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_table()
    elif choice == "2":
        insert_from_csv()
    elif choice == "3":
        add_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        show_all_contacts()
    elif choice == "6":
        search_by_name()
    elif choice == "7":
        search_by_phone()
    elif choice == "8":
        delete_by_name()
    elif choice == "9":
        delete_by_phone()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")