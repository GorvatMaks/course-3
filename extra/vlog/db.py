import settings
import sqlite3
from pprint import pprint


conn = None
curs = None

def do(query, params = None):
    curs.execute(query, params)
    conn.commit()


def close():
    curs.close()
    conn.close()


def open():
    global conn, curs
    conn = sqlite3.connect(settings.DB_URL)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

def getUser():
    pass

def getAuthData():
    pass

def updateUser(data):
    pass

def getPostsByCategory(category_name):
    pass

def getIdByCategory(category_id):
    pass

def addPost(category_id, post, title, filename):
    pass

def delPost(post_id):
    pass