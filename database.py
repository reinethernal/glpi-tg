import sqlite3
from sqlite3 import Error
from config import DATABASE_PATH

# Create connection to the SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        print(f"Connection to SQLite database successful with path {DATABASE_PATH}")
    except Error as e:
        print(e)

    return conn

# Create tables for user and operator information, request and ticket data
def create_tables():
    conn = create_connection()
    c = conn.cursor()

    # Create users table
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    telegram_id INTEGER UNIQUE,
                    glpi_username TEXT UNIQUE,
                    glpi_password TEXT
                )""")
    print("Created users table")

    # Create operators table
    c.execute("""CREATE TABLE IF NOT EXISTS operators (
                    id INTEGER PRIMARY KEY,
                    telegram_id INTEGER UNIQUE,
                    glpi_groupid INTEGER,
                    glpi_username TEXT UNIQUE,
                    glpi_password TEXT
                )""")
    print("Created operators table")

    # Create requests table
    c.execute("""CREATE TABLE IF NOT EXISTS requests (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    title TEXT,
                    description TEXT,
                    status TEXT DEFAULT 'new',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )""")
    print("Created requests table")

    # Create tickets table
    c.execute("""CREATE TABLE IF NOT EXISTS tickets (
                    id INTEGER PRIMARY KEY,
                    request_id INTEGER,
                    operator_id INTEGER,
                    title TEXT,
                    description TEXT,
                    status TEXT DEFAULT 'new',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(request_id) REFERENCES requests(id),
                    FOREIGN KEY(operator_id) REFERENCES operators(id)
                )""")
    print("Created tickets table")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()