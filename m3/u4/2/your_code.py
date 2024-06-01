import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('m3/u4/1/GoogleApps.csv')

df["Installs"].plot(kind = "area")
plt.show()

df[df["Type"] == "Paid"]["Price"].plot(kind = "box")
plt.show()

df["Installs"].plot(kind = "bar")
plt.show()