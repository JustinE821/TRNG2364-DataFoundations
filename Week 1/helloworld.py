print("Hello, World!")
print('Hello, World')

##Data types in Python
# variables can be declared implicitly without specifying datatype
a = "String of words and characters and yada yada"
explicitString: str = "My explicit string"
#Number types
#Integer - int - whole nums
b = 7
explicitInt: int = 7

#float - Float - decimal nums
c = 3.14159
explicitFloat: float = 3.234

#Boolean - True/False 
#Falsey Values: 0, 0.0, None, empty string "", empty list[], or tuple, or dict
#Truthy values: anything else
d = True
explicitBool: bool = False

if b:
    print("b is True")
else:
    print("b is False")

#Nonetype - None - represents a null value or the absense of a value
e = None
explicitNone: None = None


print(a, b)
print(explicitString)
print(b + c)

print("I have", b, "cats in my house.")

f = 74
print(f)
f = "Green"
print(f)

#Casting lets us specify the type we want to convert into
a = str(9)
b = int(9)
c = float(9) # 9.0
d = bool(9) # Will be True
print(a, b, c, d)

#check datatype using the type() function

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Variables are case sensitive
A = "uppercase A"
print(A)
a = "lowercase a"
print(a)

#W can assign multiple variables in one line
dog = DOG = Dog = dOg = "Beagle"
print(dog, DOG, Dog, dOg)