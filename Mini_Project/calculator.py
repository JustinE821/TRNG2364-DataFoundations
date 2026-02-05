


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def matrix_multiplication(df1, df2):
    return df1



def divide(x, y):
    try:
        return x / y
    except(ZeroDivisionError):
        print("You cannot divide by zero!")
    except(Exception):
        print("You really messed this up didn't you?")

x = 5
y = 4
print(add(x, y))
print(subtract(x, y))
print(multiply(x, y))
print(multiply(x, "djewoifj"))

print(divide(x, y))
print(divide(x, 0))
print(divide(4, "drfwr"))