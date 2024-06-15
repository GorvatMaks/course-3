import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv("m4/u1/titanic.csv")

#print(df.info())

df.drop(["PassengerId", "Name","Ticket","Cabin"], axis=1, inplace=True)

df["Embarked"].fillna("S", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
#print(df.info())

def ReturnSex(sz):
    if sz == "male":
        return 1
    return 0

df["Sex"] = df["Sex"].apply(ReturnSex)

df[list(pd.get_dummies(df["Embarked"]).columns)] = pd.get_dummies(df["Embarked"])

df.drop(["Embarked"], axis=1, inplace=True)

#print(df)

x = df.drop("Survived", axis=1)
y = df["Survived"]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25)
#print(x_train, x_test, y_train, y_test)

sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

#print(x_test)

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train, y_train)
#print(classifier)
y_pred = classifier.predict(x_train)

prenet = accuracy_score(y_train,y_pred) * 100
print(prenet)

 