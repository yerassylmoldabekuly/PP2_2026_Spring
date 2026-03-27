import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="pp2_db",
        user="postgres",
        password="qwerty12345"
    )
    print("Connected successfully")
    conn.close()
except Exception as e:
    print("Error:", e)