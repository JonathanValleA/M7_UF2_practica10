import matplotlib.pyplot as plt
import pandas as pd

import ejercicio3 as ejercicio3

ejercicio3.velocidadMicro()

df = pd.read_csv("test.csv")
x = df["id"]
y = df["clock_speed"]
colors = 'blue'
plt.xlabel('clock_speed')
plt.bar(x,y, color=colors)
plt.show()