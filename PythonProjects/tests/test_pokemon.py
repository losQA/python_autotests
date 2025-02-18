import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'de1f797005207f74607a99b67f6fbfea'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN} 
TRAINER_ID = '18473'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_respons():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'bmhm'

   