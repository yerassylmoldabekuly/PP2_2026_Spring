from connect import connect_db


def execute_sql_file(filename):
    conn = connect_db()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        sql = file.read()
        cur.execute(sql)

    conn.commit()
    cur.close()
    conn.close()
    print(f"{filename} executed successfully.")


def search_by_pattern(pattern):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()

    print("\nSearch results:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def get_page(limit_count, offset_count):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit_count, offset_count))
    rows = cur.fetchall()

    print("\nPaginated results:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def insert_or_update_user(username, phone):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("CALL insert_or_update_user(%s, %s)", (username, phone))
    conn.commit()

    cur.close()
    conn.close()
    print(f"User {username} inserted/updated successfully.")


def insert_many_users(usernames, phones):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("CALL insert_many_users(%s, %s)", (usernames, phones))
    conn.commit()

    cur.close()
    conn.close()
    print("Many users inserted/updated.")


def delete_user(value):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (value,))
    conn.commit()

    cur.close()
    conn.close()
    print(f"Delete procedure executed for: {value}")


def show_all_users():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook ORDER BY id")
    rows = cur.fetchall()

    print("\nAll users:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def main():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Execute procedures.sql")
        print("2. Execute functions.sql")
        print("3. Insert or update one user")
        print("4. Insert many users")
        print("5. Search by pattern")
        print("6. Get paginated data")
        print("7. Delete user by username or phone")
        print("8. Show all users")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            execute_sql_file("procedures.sql")

        elif choice == "2":
            execute_sql_file("functions.sql")

        elif choice == "3":
            username = input("Enter username: ")
            phone = input("Enter phone: ")
            insert_or_update_user(username, phone)

        elif choice == "4":
            n = int(input("How many users do you want to add? "))
            usernames = []
            phones = []

            for i in range(n):
                username = input(f"Enter username {i + 1}: ")
                phone = input(f"Enter phone {i + 1}: ")
                usernames.append(username)
                phones.append(phone)

            insert_many_users(usernames, phones)

        elif choice == "5":
            pattern = input("Enter pattern to search: ")
            search_by_pattern(pattern)

        elif choice == "6":
            limit_count = int(input("Enter limit: "))
            offset_count = int(input("Enter offset: "))
            get_page(limit_count, offset_count)

        elif choice == "7":
            value = input("Enter username or phone to delete: ")
            delete_user(value)

        elif choice == "8":
            show_all_users()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()