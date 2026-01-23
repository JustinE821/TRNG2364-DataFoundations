import os #Module needed to delete a file


#File handling refers to the process of creating, opening, reading, 
# #writing, and deleting files using python
#Python has built-in functions and methods that make this easy

#Important to know for data persistence and processing
#automation of many real-world tasks
# handling large data sets

#open() - is the key function and takes 2 parameters: filename and mode
#4 different modes available
#"r" - read, the default mode for reading and throws an error if the file does not exist
#"a" - append the end of a file and it creates the file if it does not exist
#"w" - write and if a file already has data, it will be overwritten
#"x" - create, returns an error if the file fails to be created

#we can determine if the file should be handed as binary or text using "b" and "t" respectively


try:
    my_file = open('./Week 1/resources/MyNewFile.txt', "x") #Created our new file
except(FileExistsError):
    print("Already exists")


my_second_file = open('./Week 1/resources/MySecondFile.txt', "+w")

my_file = open('./Week 1/resources/MyNewFile.txt', "r")
#print(my_file.read())

#reads a single line, calling it again will read the second line
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

#we can also specify to only read first x characters
#Read functions also keep track of where we are
# print(my_file.read(3))
# print(my_file.read(4))

#It is best practice to close a file oncce we are done with it
my_file.close()
my_second_file.close()

#we can access files using exact paths(IT NEEDS TO USE FORWARD SLASHES)
#we can use the 'with' statement to automatically close the file after the suite finishes
#with open("C://Users/justi/Desktop/RevFolder/TRNG2364-DataFoundations/Week 1/resources/MyNewFile.txt", "r") as my_third_file:
#print(my_third_file.read())

pokemon_team = []

for p in range(6):
    pokemon = input("Enter a Pokemon for your team: ")
    pokemon_team.append(pokemon)

with open('./Week 1/resources/MyPokemonTeam.txt', "+w") as teamFile:
    for p in pokemon_team:
        teamFile.write(p + "\n")
    print("Your Pokemon team has been saved!")

with open('./Week 1/resources/MyPokemonTeam.txt', "r") as team_file:
    print("Your Pokemon team consists of: ",team_file.read())

# it is best practice to check if a file exists before trying to delete it
if os.path.exists('./Week 1/resources/MySecondFile.txt'):
    os.remove('./Week 1/resources/MySecondFile.txt')
    print("File deleted successfully")
else:
    print("Something went wrong, file was not deleted")

