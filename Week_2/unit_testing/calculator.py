# A simple calculator class with some simple mathematical functions to write tests against
import array


def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):

    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y



import re

string = "thisis_an-ema9il@900."
regex_filter = r"^[A-Za-z0-9_-]+@[a-zA-Z0-9]+[.]([a-zA-Z]{1}$|[a-zA-Z]{2}$|[a-zA-Z]{3}$)"
if re.search(regex_filter, string):
    print("Passed filter")
else:
    print("Failed")

numbers = array.array('i', [3,1,4,2,5,67])
print(numbers)
numbers_sorted = sorted(numbers)
print(numbers_sorted)
numbers_sorted.append(654)
numbers_sorted.remove(67)
print(numbers_sorted)

str_arr = array.array('u', "Naner")
str_arr = sorted(str_arr)

print(str_arr)

int_set = set([3,456,2,7,3,2,123,654,32])
print(int_set)

dict1 = dict()
dict1["Hi"] = "What up?"
print(dict1.get("Hi"))
print(dict1.copy())
