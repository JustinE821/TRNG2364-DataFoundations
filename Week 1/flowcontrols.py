import functions




#control flow statements in python

#for

loop_pets = ["Charlie", "Sophie", "Soup", "Winston", "Bella"]

#loops through a collection of items
#dor x in collection, do something
for pet in loop_pets:
    print(pet)

#while
#good while a certain condition is true
count = 0
while count < 5:
    print("from the while loop")
    count += 1

#We can nest loops and mix and match
#BUT, if you find yourself using 3 or more loops deep, there is likely a better way

#If-else
#we can check a condition and execute a block of code based on the output(true/false)
#be careful: python relies on indentation to know where a block of code ends

cheese = 4
if cheese > 5:
    print("Cheese is the greatest!")
else:
    print("Cheese is not the greatest")

#we can check multiple conditions using elif
#this will execute the first true block and skip the rest
#these are good for checking multiple mutually exclusive conditions
score = 33
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")


#shorthand if
a = 9
b = 9
c = 70

if a > b: print("a is greater than b")
print("a is my favorite") if a > b else print("b is my favorite")

#multiple conditions using our logical operators
if a > b and c > a:
    print("Both conditions are true!")
if a > b or c < a:
    print("At least one condition is true")
if not a < b:
    print("a is not less than b")

if a > 5:
    print("a is more than 5")
    if a > 10:
        print("and more than 10")
    else:
        print("but not more than 10")

#match-case (known as switch statements in other languages)
choice = input(f"select a number between 1 and 3")

match choice:
    case "1":
        print("you chose case number 1")
    case "2":
        print("you chose case number 2")
    case "3":
        print("you chose case number 3")
    case _: #the default case if none of the above cases are true
        print("You did not follow directions")




        