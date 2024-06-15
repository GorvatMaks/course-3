import pandas as pd
df = pd.read_csv('m3/u3/1/GooglePlayStore_wild.csv')
# Виведи інформацію про всі DataFrame, щоб дізнатися, які стовпці потребують очищення
# Скільки в датасеті додатків, у яких не вказано (NaN) рейтинг (Rating)?
#print(df.info())
#print(df[pd.isnull(df['Rating'])])


# Заміни порожнє значення ('NaN') рейтингу ('Rating') для таких програм на -1.
#df["Rating"].fillna(-1, inplace=True)
#print(df['Rating'])

#print(df.dropna().info())

#df['Reviews']= df['Reviews'].apply(int)
#print(df.info())

#a = [1, 2, 3, 4, 5, 6, 10]

#print(a[2:7])

#print(a[:-4])

#def Makeprice(pr):
 #   if pr[0] == '$':
#       return float(pr[1:])
 #   return 0

#df['Price']= df['Price'].apply(Makeprice)
#print(df.info())
#def Makeprice(pr):
#    if pr[0] == '$':
 #      return float(pr[1:])
 #   return 0

#df['Price']= df['Price'].apply(Makeprice)
#print(df.info())

def Makeprice(sz):
    if sz[-1] == 'k':
       return float(sz[:-1])
    if sz[-1] == 'M':
       c = float(sz[:-1])
       a = c * 1024
       return a
    return 0

df['Size']= df['Size'].apply(Makeprice)
print(df.info())



# Визнач, яке ще значення розміру ('Size') зберігається в датасеті крім Кілобайтів та Мегабайтів, заміни його на -1.
# Перетвори розміри додатків ('Size') у числовий формат (float). Розмір усіх програм повинен вимірюватися в Мегабайтах.

# Чому дорівнює максимальний розмір ('Size') додатків з категорії ('Category') 'TOOLS'?

# Бонусні завдання
# Заміни тип даних на цілий (int) для кількості установок ('Installs').
# У записі кількості установок ('Installs') знак "+" необхідно ігнорувати.
# Тобто, якщо в датасеті кількість установок дорівнює 1,000,000+, необхідно змінити значення на 1000000

# Згрупуй дані за категорією ('Category') та цільовою аудиторією ('Content Rating') будь-яким зручним для тебе способом,
# Порахуй середню кількість установок ('Installs') у кожній групі. Результат округлили до десятих.
# В отриманій таблиці знайди клітинку з найбільшим значенням.
# До якої вікової групи та типу додатків відносяться дані з цієї клітинки?

# У якої програми не вказаний тип ('Type')? Який тип там потрібно записати залежно від ціни?

# Виведи інформацію про все DataFrame, щоб переконатися, що очищення пройшло успішно