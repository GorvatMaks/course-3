import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv("m4/u2/train.csv")

print(df.info())

df.drop(["sex","bdate","has_photo","has_mobile","graduation"], axis=1, inplace=True)

print(df.info())

df["education_form"].fillna('Part-time', inplace=True)

#порахувати кожне(к-ль) значення education_form і з них вивести середнє значення