import pandas as pd

df = pd.read_csv('m3/u1/1/GoogleApps.csv')

cont = df.groupby(by = 'Content Rating')['Size'].mean()
conten = df.groupby(by = 'Content Rating')['Size'].agg(['min','mean','max'])


contents = df.groupby(by = 'Content Rating')['Category'].agg(['min','mean','max'])

print(contents)

