import array as ar
#or import array



#Functions are how we package useful functionality into reusable blocks to use when needed

#Creating a function - we use the def keyword, name the function, give it parameters
#then we write the code we want to execute

#function with 2 params
def addition_function(x, y:int):
    return x + y

#no params function
def bark():
    print("woof")

#calling our functions
sum = addition_function(9, 10)
print(sum)
bark()

print(addition_function("my cat", "Wonton"))

#Scopes
#are areas of the code where an object/variable/function can be called upon and used

#Local: variables declared inside a block of code and can only be used inside that block
def local_variable():
    message = "Hi 'yall"
    print(message)

    #Enclosed: function is enclosed in another function
    #this function can access variables from the outer function
    def enclosed():
        message = "enclosed hi y'all"
        print(message)
    
    enclosed()
    print(message)

local_variable()

#Global: accessed from anywhere within the file they are declared in
#as well as other files IF they are brought in via import
myCat = "Wonton"

#Default: Built in default python methods where all keywords live and can be accessed from anywhere


#Modules in Python are simply files in which python code is written
#to use different modules, we have to import them into the module we want to use it from
#modules also support aliases using the 'as' keyword

#arrays are not technically build into python, we have to import the array module
#contain elements of the same type, stored sequentially, and indexed from 0
#array(typecode, initializer)

#Typecode: this ia a single character that specifies the type of data stored in the array
# 'i' : stored integer (4 bytes)
# 'f' : floating pount (4 bytes)
# 'd' : double precision floating point(8 bytes)
# 'b' : signed integer (1 byte)
# 'u' : unicode character (2 bytes*)
# 'l' : signed long integer (4 bytes)(platform dependent)

#initializer: this is an optional parameter that initializes the array with elements
#it can be a list, a tupel, or any other iterable containing the initial values for the array

int_array = ar.array('i', [1,2,77,3,25,99,51])
print(int_array[2])
my_subset = int_array[1:4]
print(my_subset)

for item in int_array:
    print(item)

#find the length
print(len(int_array))

#sort array in ascending order
print(sorted(int_array))

#Lambda function AKA anonymous functions
#small, single line functions that can have any number of arguments, but only one single expression
#lambda args: expression

add = lambda x, y: x + y
print(add(3, 4))


pokedex = [("Bulbasaur", 1),
           ("Lapras", 131),
           ("Eevee", 133),
           ("Cubone", 104),
           ("Gengar", 94)
]

dictionary_pokedex = {2:"Ivysaur", 3:"Venusaur"}
print(pokedex[1][1])


pokedex.sort(key = lambda x: x[1], reverse = True)
print(pokedex)