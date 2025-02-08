import settings
import sqlite3
from pprint import pprint


conn = None
curs = None

def do(query, params = []):
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

def getPostsByCategory(category_id):
    open()
    query = "SELECT * FROM post WHERE category_id=?"
    
    do(query, params=[category_id])
    all_post = curs.fetchall()
    
    close()
    return all_post

def getIdByCategory(category_name):
    open()
    query = "SELECT id FROM category WHERE name=?"
    
    do(query, params=[category_name])
    all_id = curs.fetchone()['id']
    
    close()
    return all_id

def addPost(category_id, post, title, filename):
    pass

def delPost(post_id):
    pass