#Math module contains many important mathematic constants and functions
import math
import json
import re

#min() and max() functions find the smallest and the largest values
# in an iterable(collections) or amongst multiple args
x = min(2, 7, 99, 18, 4)
y = max(6, 17, 81, 100, 42)
print(f"Minimum value: {x}\nMaximum value: {y}")

#abs() function returns the absolute value of a number
z = abs(-7.23)
print("Absulute value: ", z)

#pow() function returns the value of a number raised to the power of another number
a = pow(3,4) # 3 to the power of 4
print("Power of: ", a)
# ** keeps type, while pow() always returns float and is slightly slower

#sqrt() function returns the square root of a number, always returns float
b = math.sqrt(64)
print("Square root: ", b)

#ceil() rounds a number up to the nearest integer
c = math.ceil(4.2)

#floor() function rounds a number down to the nearest integer
d = math.floor(7.8)

print("Ceil: ", c, "\nFloor: ", d)

#pi constant represents the mathematical constant pi
p = math.pi
print(f"Pi: {p}")


#JSON
#The Json module can be used to work with JSON data
#JSON stands for JavaScript Object Notation

#We can parse JSON objects and convert them into Python dictionaries
json_data = '{"name": "Alice", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print("Name: ", data["name"])
print("Age: ", data["age"])

#We can convert Python dictionaries into JSON objects
#dict, list, tuple, string, int, floats, boolean, None 
# can all be converted to JSON using dumps() function
python_dict = {"fruit": "Apple", "Color": "Red", "Quantity": 5}
json_object = json.dumps(python_dict)
print("JSON Object: ", json_object)

#dumps() function can take additional parameters to format the JSON output
formatted_json = json.dumps(python_dict, indent = 4)
print("Formatted JSON: ", formatted_json)


#RegEx stands for regular ecpressions, which is a sequence of characters that forms a search pattern
#Useful for finding substrings, data validation, text manipulation, and more
#the re module provides support for regular expressions in Python

#search() function to search for a pattern within a string
text = "The cat and the rat are She on the roof with another cat eating cat food and wearing 3 collars and wearing a hat and 2 collars"
match = re.search("cat", text)
if(match):
    print("pattern found: ", match.group())

#we can use the findall() function to find all occurances of a pattern in a string
matches = re.findall("cat", text)
print("All occurances of 'cat'", matches)

#regex metacharacters can help us perform more complex searches
#aka wildcards
#[] - A set of characters
print(re.findall(r"[crh]at", text)) # checks for all instances of 'cat' and 'rat'


#\d - any digit 0-9
print(re.findall(r"\d", text))


# ^ - Starts with
print(re.search(r"^The", text)) #Checks iif the string starts with 'The'

# $ - Ends with
print(re.search(r"collars$", text)) #Checks iif the string ends with 'collars'

#split() function splits a string at each match of a pattern
#\s lets us split at the spaces
split_text = re.split(r"\s", "Split this text into words.")
print(split_text)

#sub() function replaces matches with a specified string
replaced_text = re.sub(r"[cr]at", "dog", text)
print(replaced_text)