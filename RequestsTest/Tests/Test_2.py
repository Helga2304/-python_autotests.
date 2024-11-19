import requests
URL = "https://api.pokemonbattle.ru/v2" 
trainer_id = "6869"

def test_trainer_name():
     response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': trainer_id})
     assert 'Джефф' in response.text
