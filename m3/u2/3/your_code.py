import pandas as pd

df = pd.read_csv('m3/u1/1/GoogleApps.csv')

makson = df.pivot_table(
    columns='Type',
    index='Content Rating',
    values='Size',
    aggfunc=['min','mean']
)

print(makson)



#1)
'''
fb = (df['Category'].value_counts())
fbb = fb['BUSINESS']
print(fbb)'''



#2)
'''
fb = (df['Content Rating'].value_counts())
fbb = fb['Teen']
bb = fb['Everyone 10+']

gh = fbb/bb

print(gh)
'''



#3)
#1
'''
b = (df[df['Type'] == 'Paid']['Rating'].mean())
print(b)
'''



#2
'''
a = (df[df['Type'] == 'Free']['Rating'].mean())
b = (df[df['Type'] == 'Paid']['Rating'].mean())

c = b-a
print(c)
'''


#4)
'''
contents = df.groupby(by = [df['Rating' ]== "COMICS"])['Size'].agg(['min','max'])
print(contents)
'''
#5)
#1
#fb = (df[df['Rating']== 4.5]['Category'].value_counts())
#fbb = fb["FINANCE"]
#print(fbb)


#2
#mb = (df[df['Rating']== 4.9]['Type'].value_counts())
#fre = mb["Free"]
#plat = mb["Paid"]
#rez = fre/plat
#print(rez)