import requests

URL = "https://api.pokemonbattle.ru/v2"  
TOKEN = 'afe659512a4d626524fb77c1ad8014a5'
headers = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
trainer_id = "6869"

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': trainer_id})
    assert response.status_code == 200
   