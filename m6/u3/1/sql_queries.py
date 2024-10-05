import sqlite3
from pprint import pprint
conn = sqlite3.connect("m6/u3/1/Artistc.db")

curs = conn.cursor()


# Запитання 1. Інформація про скількох художників представлена у базі даних?
curs.execute("SELECT * FROM artists")

data = curs.fetchall()
print("К-ль художників в цьому файлі =",len(data))

pprint(data)

# Запитання 2. Скільки жінок (Female) у базі?
curs.execute('SELECT * FROM artists WHERE Gender="Female" ')
data = curs.fetchall()
print("К-ль художниць в цьому файлі =",len(data))


# Запитання 3. Скільки людей у базі даних народилися до 1900 року?
curs.execute('SELECT * FROM artists WHERE "Birth Year"<=1900 ') 
data = curs.fetchall()

print("К-ль художників народженні до 1900року в цьому файлі =",len(data))


# Запитання 4*. Як звати найстаршого художника?
curs.execute('SELECT * FROM artists WHERE "Birth Year"<=1900 ORDER BY "Birth Year" ASC') 
data = curs.fetchall()

print('Найстарший художний в файлі є',data[0][1])
