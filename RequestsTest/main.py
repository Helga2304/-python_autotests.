import requests
import json

# URL для API
URL = "https://api.pokemonbattle.ru/v2"  
TOKEN = 'afe659512a4d626524fb77c1ad8014a5'
# Создание покемона
create_pokemon_url = f"{'https://api.pokemonbattle.ru/v2'}/pokemons"
create_pokemon_body = {
    "name": "generate",
    "photo_id": -1
}
headers = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
response = requests.post(create_pokemon_url, headers=headers, json=create_pokemon_body)
print("Создание покемона:", response.json())
print(response.text)

# Смена имени покемона
change_name_url = f"{'https://api.pokemonbattle.ru/v2'}/pokemons"
change_name_data = {
    "pokemon_id": "140863",  
    "name": "raichu",
    "photo_id": 2
}
response = requests.put(change_name_url, headers=headers, json=change_name_data)
print("Смена имени покемона:", response.json())
print(response.text)

# Поймать покемона в покебол
catch_pokemon_url = f"{'https://api.pokemonbattle.ru/v2'}/trainers/add_pokeball"
catch_pokemon_data = {
       "pokemon_id": "140863"   
}
response = requests.post(catch_pokemon_url, headers=headers, json=catch_pokemon_data)
print("Поймать покемона в покебол:", response.json())
print("Содержимое ответа:", response.text)