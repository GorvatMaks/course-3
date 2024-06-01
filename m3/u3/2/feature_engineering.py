import pandas as pd
df = pd.read_csv('m3/u3/2/GooglePlayStore_wild.csv')

def listChanr(chanr):
    listplit = chanr.split(";") 
    return len(listplit)

df["LenChaners"] = df["Genres"].apply(listChanr)

print(df["LenChaners"].max())


# Очищення даних із першого завдання

# Заміни тип даних на дробове число (float) для цін додатків (Price)

# Обчисли, скільки доларів розробники заробили на кожному платному додатку

# Чому дорівнює максимальний дохід ('Profit') серед платних додатків (Type == 'Paid')?

# Створи новий стовпець, у якому зберігатиметься кількість жанрів. Назви його 'Number of genres'

# Яка максимальна кількість жанрів (Number of genres) зберігається в датасеті?

# Бонусне завдання
# Створи новий стовпець, що зберігає сезон, в якому було зроблено останнє оновлення (Last Updated) програми. Назви його 'Season'

# Виведи на екран сезони та їх кількість у датасеті
