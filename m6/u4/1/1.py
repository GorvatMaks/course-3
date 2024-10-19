import sqlite3
from pprint import pprint
conn = None

curs = None

def createTable():
    open()
    do('PRAGMA foreign_keys=on')

    do('''
        CREATE TABLE IF NOT EXISTS quiz(
            id INTEGER PRIMARY KEY,
            name VARCHAR)                        
    ''')


    do('''
        CREATE TABLE IF NOT EXISTS question(
            id INTEGER PRIMARY KEY,
            question VARCHAR, 
            answer VARCHAR,
            wrong1 VARCHAR,
            wrong2 VARCHAR,
            wrong3 VARCHAR
        )                              
    ''')


    do('''
        CREATE TABLE IF NOT EXISTS  quiz_content(
            id INTEGER PRIMARY KEY,
            quiz_id INTEGER,
            question_id INTEGER,
            FOREIGN KEY (question_id) REFERENCES question (id),
            FOREIGN KEY (quiz_id) REFERENCES quiz (id)
        )                        
    ''')
    
    close()


def do(query):
    curs.execute(query)
    conn.commit()


def close():
    curs.close()
    conn.close()


def open():
    global conn, curs
    conn = sqlite3.connect("m6/u4/1/Quiz.db")

    curs = conn.cursor()


def clear_db():
    open()
    do('DROP TABLE IF EXISTS quiz_content')
    do('DROP TABLE IF EXISTS question')
    do('DROP TABLE IF EXISTS quiz')
    close()


def add_question():
    questions = [
        ('Хто мій вчитель з програмування?', 'Володмир','бублик','ластівка','я'),
        ('Скільки місяців на рік мають 28 днів?', 'Всі', 'Один', 'Жодного', 'Два'),
        ('Яким стане зелена скеля, якщо впаде в Червоне море?', 'Мокрим', 'Червоним', 'Не зміниться', 'Фіолетовим'),
        ('Якою рукою краще розмішувати чай?', 'Ложкою', 'Правою', 'Лівою', 'Любою'),
        ('Що не має довжини, глибини, ширини, висоти, а можна виміряти?', 'Час', 'Дурність', 'Море', 'Повітря')
    ]
    open()
    curs.executemany(''' 
        INSERT INTO question (question, answer, wrong1, wrong2, wrong3)
        VALUES (?,?,?,?,?)
        ''', questions)
    conn.commit()
    close()

def add_quiz():
    quizs = [
        ('Початковий квіз',),
        ('Середній квіз',),
        ('Хард квіз',)
    ]
    open()
    curs.executemany('''
        INSERT INTO quiz (name)
        VALUES (?)
        ''', quizs)
    conn.commit()
    close()


def add_question_on_quiz():
    open()
    do('PRAGMA foreign_keys=on')

    query = '''
        INSERT INTO quiz_content (quiz_id, question_id)
        VALUES (?,?)
        '''
    input1 = input("Чи додати зв'зок?(Y/N)")
    
    while input1 != 'N':
        quiz_input = int(input("Id квіза"))
        question_input = int(input("Id запитання"))
        curs.execute(query,[quiz_input, question_input])
        conn.commit()
        input1 = input("Чи додати зв'зок?(Y/N)")
    close()

def show(Table):
    open()
    curs.execute("SELECT * FROM " + Table)
    data = curs.fetchall()
    pprint(data)
    close()

def showTables():
    show("question")    
    show("quiz")    
    show("quiz_content")

def getQuestion(question_id, quiz_id):
    open()
    query = ''' 
    SELECT quiz_content.id, question.question, question.answer, question.wrong1, question.wrong2, question.wrong3
    FROM question, quiz_content
    WHERE quiz_content.question_id == question.id
    AND quiz_content.id >= ? 
    AND quiz_content.quiz_id == ?
    ORDER BY quiz_content.id
    '''
    curs.execute(query,[question_id, quiz_id])
    rezalt = curs.fetchone()
    close()
    return rezalt


#clear_db()
#createTable()
#add_question()
#add_quiz()
showTables()
#add_question_on_quiz()
print(getQuestion(1,1))