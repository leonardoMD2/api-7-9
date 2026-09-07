import sqlite3

def get_connection():
    conn = sqlite3.connect("tienda.db")
    conn.row_factory = sqlite3.Row  # columna por nombre res["id"]
    try:
        yield conn
    finally:
        conn.commit()
        conn.close()

def initDb():
    conexion = sqlite3.connect("tienda.db")
    conexion.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, nombre TEXT, stock INTEGER, precio REAL)")
    conexion.commit()
    conexion.close()