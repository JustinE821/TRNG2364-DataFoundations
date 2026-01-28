#In python we can have named tuples
#they allow you to access theif elements by name and index
#Named tuples are part of the collection module and provide a way to create self documenting
#immutable data structures
#good for reading an object or rows from sql queries, CSVs, or API responses

from collections import namedtuple, OrderedDict, Counter

#to create a named tuple, we use the namedtuple() factory function
point = namedtuple('Point', ['x', 'y'])
#We can create an instance of point
p = point(x=1, y=5)
#Access using a field name
print(p.x, p.y)


#Access items using index
print(p[0])

#Access using a getattr()
print(getattr(p, 'y'))

#More precise example
user = namedtuple("User", ["id", "username", "password", "email"])

my_user = user(12, "JonDoe", "password", "JonDoe@email.com")
print(my_user.username, my_user.password)



#Ordered Dictionaries
#are good for when you are using items in a specific order
#great for configuration settings or environment variables
#also from the collections module

config = OrderedDict()

#set defaults
config["timeout"] = 5
config["retries"] = 3
config["two-factor"] = True

#we can overide values that are already set
config["timeout"] = 10

#Set certain items to always be considered last
config.move_to_end("timeout")

#we can inspect the order
for key, value in config.items():
    print(key, value)


#Counters
#counters allow us to count things without writing loops
#comes from the collections module

words = ["fruit", "meat", "fruit", "fruit", "dairy", "veggies", "dairy", "grains", "legumes"]
count = Counter(words)
print(count)

print(count["fruit"])