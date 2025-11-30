import sqlite3

def connect():
    conn = sqlite3.connect("community.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            location TEXT,
            description TEXT
        )
    """)
    conn.commit()
    return conn

# Connect & create table on import
connect()

def add_event(name, location, description):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events(name, location, description) VALUES (?, ?, ?)",
                   (name, location, description))
    conn.commit()
    conn.close()

def get_events():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events")
    rows = cursor.fetchall()
    conn.close()
    return rows
