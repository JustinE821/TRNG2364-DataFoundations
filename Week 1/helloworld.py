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

#Collections - variables that hold multiple values
#Collections is a module in python
#Lists, tuples, sets, and dict
'''List is a collection that is orderable and changeable and allows duplicate values
Tuple is a collection that is ordered, unchangeable, and allows duplicate vals
Set is a collection that is unordered, unchangeable, and unindexed, do NOT allow duplicate values
Dictionary is a collection that is ordered and changeable but does not allow dupe values'''

#Lists use square[] brackets and can contain different data types
#Python sees lists as objects with the datatype 'list'
fruits = ["Orange", "Strawberry", "Apple"]
fruitY_fruits = favorite_fruits = ["Strawberry", "Apple", "Banana"]
Or, St, Ap = fruits
print(Or)
print(St)
print(Ap)

mixedTypes = ["cheese", 17, False, 32.7]

#len() returns the length of a list
print(len(fruits))
print(len(Or))

#type() returns the data type of the list
print(type(fruits))

#access an item in the list using the item's index
print(fruits[1])
#We can also use negative indexing  which starts from the end
print(fruits[-1])
#Range of indexes
print(fruits[1:3])
#add items to a list
fruits.append("Grapes")
print(fruits)
#add items ar a specific index
fruits.insert(2, "Kiwi")
print(fruits)

#Tuples
#Tuples can contain different data types and are defined as objexts of the data type "Tuple"
animal_tuple = ("Cat", "Dog", "Bird", "Fish")
print(animal_tuple)

#len() works for tuples too
print(len(animal_tuple))

#Since tuples are immutable we cannot use the append() func
#instead we can cpnvert it to a list
animal_list = list(animal_tuple)
animal_list.append("Snake")
print(animal_list)

#Sets
#sets are created using curly braces{}
colors_set = {"blue", "green", "pink", "orange"}

#sets can use the add and remove functions for adding and removing elements
colors_set.add("brown")
colors_set.remove("orange")
print(colors_set)

#sets support intersection difference and union
second_set = {"Burger", "Fries", "Milkshake", "brown"}
intersection_set = colors_set & second_set
print("Intersection set: ", intersection_set)

difference_set = colors_set - second_set
print("Difference set: ", difference_set)

union_set = colors_set | second_set
print("Union set: ", union_set)

#Dictiionary
#Dictionaries are defined as key-value pairs with curly braces{} and separated by a colon :
#Pairs are separated by a comma
#The first values is treated as the key and the second value is treated as the value
food_dict = {"Sushi":"Fish", "Brisket":"Beef", "Pizza":"Pepperoni"}

#values() will return all values in the dict
print(food_dict.values())

#The value of a specific item can be changed by referring to its key
food_dict["Sushi"] = "Rice"
print(food_dict)

#We can add items by using index key and giving it a value
food_dict["Pickle"] = "Cucumber"
print(food_dict)


#keys() will return all keys in dict
print(food_dict.keys())

#We can check if a key exists in a dict
if "Burger" in food_dict:
    print("Yes, there is a burger in the dictionary")
else:
    print("No, there isn't a burger in this dictionary")

#Operators
#Are symbols that define operation behaviors between data types

#Arithmetic operators
# +, -, *, /, %(modulator), **(exponent), //(floor division)
print(11 + 9)
print(24 / 3)

#Assignment operators
# =, +=, -=, *=, /=, etc

#Comparison operators
# ==, !=, >=, <=, <, >

#Logical operators
# and, or, not


#Getting user input using the input() function
print("Please enter your name")
name = input()

#f stand for formatted string
#this allows us to parameterize our string
print(f"Hello {name}")

fav_color = input(f"What is your favorite color, {name} ?")
print(f"I like {fav_color} too!")