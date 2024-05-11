import pandas as pd

df = pd.read_csv('m3/u1/1/GoogleApps.csv')

makson = df.pivot_table(
    columns='Type',
    index='Content Rating',
    values='Size',
    aggfunc=['min','mean']
)

print(makson)