import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('m3/u4/1/GoogleApps.csv')

#df["Installs"].plot(kind = "hist", bins=1000 )
#plt.show()

df[df["Type"] == "Paid"]["Price"].plot(kind = "box")
plt.show()