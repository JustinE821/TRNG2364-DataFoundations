import matplotlib.pyplot as plt
import pandas as pd


'''
Python Review Challenges

Challenge 1
```
#A weather station recorded the average temperature over 7 days.
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [12, 14, 15, 13, 16, 18, 17]

#Challenge Tasks

#Create a line plot showing temperature changes over the week.

Add:

A meaningful title

X-axis label

Y-axis label

Use circle markers and a dashed line.

Highlight the warmest day with a different color.

Add a grid.

(Bonus) Annotate the warmest temperature value on the chart.

```
'''


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [12, 14, 15, 13, 16, 18, 17]


plt.plot(days, temperatures, marker="o", linestyle="dashed", color="black", label="Temp")
plt.title("Average Temperature Throughout the Week (Raleigh NC)")
plt.xlabel("Days of the week")
plt.ylabel("Temperature(F)")
plt.grid(True)
plt.annotate("18F", ["Sat", 18])
plt.axvspan("Sat", "Sun", 0, 20, color="yellow")
plt.show()









'''
Challenge 2
```

#A small shop tracked its monthly sales for the first half of the year.
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [1200, 1350, 1100, 1500, 1600, 1550]
}

df = pd.DataFrame(data)


Challenge Tasks

Use pandas to inspect the data.

Create a line plot of sales over the months using matplotlib.

Add:

A title

X-axis label

Y-axis label

Highlight the month with the highest sales.

Add a grid.

(Bonus) Display the exact sales value for the highest month on the chart.
'''


data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [1200, 1350, 1100, 1500, 1600, 1550]
}

df = pd.DataFrame(data)

plt.plot(df["Month"], df["Sales"], marker="o", linestyle="-", color="b", label="sales")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.title("Q1 and Q2 Sales 2025")
plt.grid(True)
plt.axvspan("May", "Jun", 0, 1650, color="yellow")
plt.annotate("1650", ["May", 1600])

plt.show()