import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("./steps.csv")

n_days = int(input("How many days do you want to review steps from?"))

selected_days = df.head(n_days)

max_steps = selected_days["Steps"].max()
max_column = selected_days[df["Steps"] == max_steps]

print("Max Steps: ", max_steps, "\nMin Steps: ", 
      selected_days["Steps"].min(), "\nAverage Steps: ", selected_days["Steps"].mean())

plt.bar(selected_days["Day"], selected_days["Steps"])
plt.title("Steps per day")
plt.xlabel("Days of the Week")
plt.ylabel("Steps")
plt.grid(True)

plt.bar(
    max_column["Day"],
    max_column["Steps"],
    color='r',
    zorder=6,
    label="Most Steps"



)


plt.show()