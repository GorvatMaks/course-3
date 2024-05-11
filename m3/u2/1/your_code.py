import pandas as pd

df = pd.read_csv('m3/u1/1/GoogleApps.csv')

Every = df['Content Rating'].value_counts()
Everyfin = Every['Everyone']

Teens = Every['Everyone 10+']

Rezult = Everyfin/Teens

print(Rezult)