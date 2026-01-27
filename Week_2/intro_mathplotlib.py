#Matplotlib is comprehensive library for creating static, animated, and iterable visualization
#It provides an API that is object-oriented for embedding plots into applications
#using general GUI Nkits like TKinter, wxPython, Qt, or GTK

import matplotlib.pyplot as plt

#sample data
x = [1, 2, 4, 6, 8]
y = [2, 3, 5, 7, 11]

#Create a line plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line 1')
plt.title("My Simple Line Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)
plt.show()


#Create a bar chart
categories = ["Fruit", "Vegetables", "Meat", "Dairy"]
values = [8, 11, 4, 6]
plt.bar(categories, values, color='g')
plt.title("Food in my pantry")
plt.xlabel("Food Categories")
plt.ylabel("Number of items")
plt.show()


#Create a scatterplot
x_scatter = [9, 81, 43, 66, 12, 9]
y_scatter = [100, 5, 45, 25, 49, 8]
plt.scatter(x_scatter, y_scatter, color="r")
plt.title("My Scatter Plot")
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
