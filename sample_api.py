from xml.etree.ElementTree import indent

import requests
import json

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.ok:
        return response.json()
    else:
        print(f"Failed to fetch pokemon name: {name}")


pokemon_info = get_pokemon_info("pikachu")
if pokemon_info:
    print(pokemon_info["name"])
    print(pokemon_info["id"])
