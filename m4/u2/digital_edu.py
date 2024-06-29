import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv("m4/u2/train.csv")

#print(df.info())

df.drop(["sex","bdate","has_mobile","graduation","relation","people_main","career_start","career_end"], axis=1, inplace=True)

#print(df.info())

df["education_form"].fillna('Part-time', inplace=True)
df["city"].fillna('Moscow', inplace=True)
df["occupation_type"].fillna('university', inplace=True)
df["occupation_name"].fillna('"ТОГУ (бывш. ХПИ, ХГТУ)"', inplace=True)
#print(df.info())

def true_false(yu):
    if yu == "False":
        return 0
    return int(yu)




df["life_main"] = df["life_main"].apply(true_false)
print(df["life_main"])