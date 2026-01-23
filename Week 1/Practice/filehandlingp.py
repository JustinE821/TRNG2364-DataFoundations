import os
import requests as req
import json


err = req.exceptions.RequestException


#This file is made to be an introductory text of api calls and json reading



#This function calls the pokemon api to return a desired number of pokemon, 
# or 20 if the amount is not specified
def get_pokemon_list(pokemon_count: int = 20):


    URL = f"https://pokeapi.co/api/v2/pokemon/?offset=0&limit={pokemon_count}"



    try:
        res = req.get(URL)

        print("Http get request successful")

        if res.status_code == 200:
            pokemon = res.json()
            pokemon_names = list()
            for mons in pokemon["results"]:
                pokemon_names.append(mons["name"])
                #print(mons)
            return pokemon_names


    except(err):
        print("Http request invalid")
    
    return None


#This method allows you to type a pokemon name in and get its id
def get_pokemon_id(name: str = "Ditto"):
        
    URL = f"https://pokeapi.co/api/v2/pokemon/{name}"



    try:
        res = req.get(URL)

        print("Http get request successful")

        if res.status_code == 200:
            pokemon_json = res.json()
            #pokemon_names = list()
            pokemon_moves = pokemon_json["moves"]
            for types in pokemon_json:
                print(types)
            
            #for move in pokemon_moves:
                #print(pokemon_moves)
            #    print()
            

            return pokemon_json["id"]#, pokemon_json["moves"]["name"]]


    except(err):
        print("Http request invalid")
    
    return None




print(get_pokemon_id())




# pokemon_list = get_pokemon_list(151)

# #Check if list is empty
# if(pokemon_list != None):

#     #Prints pokemon names individually
#     for pokemon in pokemon_list:
#         print(pokemon)
#     #Line below can be used to print the list
#     #print(pokemon_list)

# print(get_pokemon_list(25))