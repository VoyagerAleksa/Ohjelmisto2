import sqlite3

conn = sqlite3.connect("flight_game.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS airport (
    ident TEXT PRIMARY KEY,
    name TEXT,
    municipality TEXT
);
""")

# Добавь сюда свои аэропорты вручную
airports = [
    ("EFHK", "Helsinki Vantaa Airport", "Helsinki"),
    ("EFRO", "Rovaniemi Airport", "Rovaniemi"),
    ("EFKU", "Kuopio Airport", "Kuopio"),
    ("EFPO", "Pori Airport", "Pori")
]

cur.executemany("INSERT OR REPLACE INTO airport VALUES (?, ?, ?)", airports)

conn.commit()
conn.close()

print("SQLite база flight_game.db создана!")