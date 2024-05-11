import pandas as pd
df = pd.read_csv('m3/u1/1/GoogleApps.csv')

# Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?

print(df[df['Type'] == 'Paid']['Price'].min())


#print(df['Last Updated'].min())
#(df['Size'].min())

#c = b/a
#print(c)



#Визначити середню кількість завантажень (Installs) безкоштовних 
#програм (Type == 'Free'), рейтинг (Rating) яких перевищує 4.9.


#print(df[
#             (df['Rating'] > 4.9) | (df['Type'] == 'Free')
#         ]['Installs'].mean())



#print(df[df['Rating'] > 4.5]['Installs'].mean())







# Чому дорівнює медіанна (median) кількість установок (Installs)додатків із категорії (Category) "ART_AND_DESIGN"?
print(df[df['Category']== "ART_AND_DESIGN"]['Installs'].median())


# На скільки максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')
#більше максимальної кількості відгуків для платних програм (Type == 'Paid')?
a = (df[df['Type'] == 'Free']['Reviews'].max())
b = (df[df['Type'] == 'Paid']['Reviews'].max())

c = a - b
print(c)

# Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')?
print(df[df['Content Rating']== "Teen"]['Size'].min())

# *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?


# *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
# з кількістю установок (Installs) понад 10000?
