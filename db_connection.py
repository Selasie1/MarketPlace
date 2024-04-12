import psycopg2


# PostgreSQL connection (destination db)
def connect_postgres():
    conn = psycopg2.connect(host="localhost", database="MarketDatabase", port=5432, user="postgres", password="hello")
    cur = conn.cursor()
    return cur, conn


# Assign the cursor and connection functions to variables

pgcur, pgcon = connect_postgres()
