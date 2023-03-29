import requests


try:

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/pikachu")

    pokemons = response.json()

    i = 1
    for pokemon in pokemons['results']:
        print(i,pokemon['name'],pokemon['height'])

    


except(Exception,requests.ConnectionError) as error:
    print("Ocorreu um erro - ",error)