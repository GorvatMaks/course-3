import pandas as pd

df = pd.read_csv("m4/u1/titanic.csv")

print(df.info())

df.drop(["PassengerId", "Name","Ticket","Cabin"], axis=1, inplace=True)

df["Embarked"].fillna("S", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
print(df.info())

def ReturnSex(sz):
    if sz == "male":
        return 1
    return 0

df["Sex"] = df["Sex"].apply(ReturnSex)

df[list(pd.get_dummies(df["Embarked"]).columns)] = pd.get_dummies(df["Embarked"])

df.drop(["Embarked"], axis=1, inplace=True)

print(df)