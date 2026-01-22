#Errors and Exceptions
#All exceptions are errors, but not all errors are exceptions

#Errors = problems that prevent our application from running correctly
#Ex. syntax error, there is no handling, we just have to fix it
#errors come with messages to diagnose the issue
#Syntax, indentation, name, value, type 0 division, etc.

#Exceptions - problems that are raised during runtime and can be
# Detected and handled using try-except (try-catch in java)

try:
    x = int("5")

except ValueError:
    print("Conversion has failed")

#try-except-else-finally
#Try catch blocks are in local scope*
try:
    number = int(input("Please enter a number: "))
    result = 10 / number
    print(result)

except ValueError:
    print("Invalid input. Please enter a valid integer")
except ZeroDivisionError:
    print("You cannot divide by zero")

#it is a good idea to have a generic catch-all exception block to handle anything 
#we  have not thought of
except Exception:
    print("I have no idea how you got here")

else:
    #runs only if no exception occurs
    print(f"Result: {result}")

finally:
    #runs no matter what, whether or not an exception is thrown
    print("Execution complete")

#We can manually raise(throw) an exception using the 'raise' keyword
y = 5
if y < 0:
    raise Exception("Sorry, no negative numbers allowed")

#We can also create our own custom exceptions using our own custom exception class
class MyCustomException(Exception):
    def __init__(self, message = "This is not the exception you are looking for"):
        super().__init__(message)

user_number = input("Please enter your favorite integer ")

if not type(user_number) is int:
    raise MyCustomException()
print(user_number)