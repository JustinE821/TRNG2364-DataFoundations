#Pthon is an OOP language
#It makes use of classes and objects to create our systems and applications
#classes are the blueprints, objects are generated based on those blueprints

class Animal:
    #In python, we have to override the __init__() to create our constructor
    #Notice this is double underscore
    #Double leading and trailing underscores are used for special methods 
    # that python calls automatically in certain situations(__init__(), __str__(), __len__(), etc.)
    #Passing in self references our freshly created object in our constructor

    def __init__(self, name, age):
        self.name = name
        self.__age = age #double underscores means private proerty

    #gerrer for private properties only
    def get_age(self): return self.__age

    #setter for private properties only
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than zero!")

    def speak(self):
        return f"{self.name} made a noise"


    def introduction(self):
        return f"My name is {self.name}, I am {self.get_age()} years old"

Bob = Animal("Bob", 3)
print(Bob.get_age())
print(Bob.speak())


#Pillars of OOP: Abstraction, Inheritance, Polymorphism, and encapsulation

# Abstraction -  the idea of showing only what a user needs to know and hiding the implementation details
# inheritance - child classes can reuse and extend the behavior of our parent classes
# polymorphism - (many forms) meaning one interface but multiple implementations
# Encapsulation - the practice of bundling data/attributes and methods into a single unit and
# restricting access to some of the object's components

#Inheritance demonstration inheriting from animal class
class Dog(Animal):

    def __init__(self, name, age, breed, color="Brown"): #= allows us to set default values
        super().__init__(name, age)
        self.breed = breed
        self.color = color

    #Polymorphism example - we are overriding the definition of the speak function
    def speak(self):
        return f"{self.name} barked at the mailman"

    #__str__() acts as our toString() method
    def __str__(self):
        return f"My name is {self.name}, I am a {self.color} {self.breed}"


Major = Dog("Major", 7, "German Shepard", "Black")
print(Major.__str__())
print(Major.speak())


# I did not ultimately test this fully, but this was made to prove you could inherit 2 classes, though it is really messy
class Other:
    def __init__(self, place, time):
        self.place = place
        self.time = time

    def speak(self):
        return "This is from the other class"

#Cat stuff


#Classes can inherit from multiple classes using a comma separated list
class Cat(Dog):
    def __init__(self, name, age, breed, color, hair_length):
        #Using the super method we can call the parent class constructor
        super().__init__(name, age, breed, color)
        self.hair_length = hair_length

    def scratch(self):
        return f"{self.name} has scratched the door frame"
    
    def speak(self):
        return f"{self.name} meowed at the door"
    

Ash = Cat("Ash", 2, "Maine Coone", "Gray", "Medium Hair")
print(Ash.scratch())
print(Ash.speak())
print(Ash.get_age())

Ash.set_age(3)
print(Ash.get_age())










    
        