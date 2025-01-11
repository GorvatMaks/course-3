import settings
import sqlite3
from pprint import pprint


conn = None
curs = None

def do(query):
    curs.execute(query)
    conn.commit()


def close():
    curs.close()
    conn.close()


def open():
    global conn, curs
    conn = sqlite3.connect(settings.DB_URL)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()