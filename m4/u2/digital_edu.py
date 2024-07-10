import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv("m4/u2/train.csv")

#print(df.info())

df.drop(["sex","bdate","has_mobile","graduation","relation","people_main","career_start","career_end", "langs", "occupation_name", "city", "last_seen"], axis=1, inplace=True)

#print(df.info())

df["education_form"].fillna('Part-time', inplace=True)
df["occupation_type"].fillna('university', inplace=True)
#print(df.info())

def true_false(yu):
    if yu == "False":
        return 0
    return int(yu)

def true_Form(yu):
    if yu == "Full-time":
        return 2
    if yu == "Part-time":
        return 1
    else:
        return 0
    return int(yu)

def true_Status(yu):
#TODO: поправити значення від 0 до 6 з презинтацій(слайд 31)
    if yu == "Undergraduate applicant":
        return 1
    if yu == "Student (Bachelor's)":
        return 2
    if yu == "Alumnus (Bachelor's)":
        return 3
    if yu == "Student (Master’s)":
        return 4
    if yu == "Alumnus (Master’s)":
        return 5
    if yu == "Candidate of Sciences":
        return 6
    else:
        return 0
    return int(yu)

#def seen(time):
#    sr = time[:9]
#    sr.replace('-','')
#    return int(sr)

def tupe(rey):
    if rey == "university":
        return 2
    if rey == "work":
        return 1
    else:
        return 0
    return int(rey)

df["education_form"] = df["education_form"].apply(true_Form)

df["life_main"] = df["life_main"].apply(true_false)

df["education_status"] = df["education_status"].apply(true_Status)

df["occupation_type"] = df["occupation_type"].apply(tupe)


#TODO: last_seen застосувати replace('-','') до дати години відкинути, до 2020-09-05 треба 20200905 

#df["last_seen"] = df["last_seen"].apply(seen)


x = df.drop("result", axis=1)
y = df["result"]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25)

sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_train)

prenet = accuracy_score(y_train,y_pred) * 100
print(prenet)
