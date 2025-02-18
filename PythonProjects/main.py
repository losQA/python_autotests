import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'de1f797005207f74607a99b67f6fbfea'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN} 

body_registration = {
    "trainer_token": TOKEN,
    "email": "losoleq@yandex.ru",
    "password": "spDCcg-6mxyJ5aU"
}
body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)''' 

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation )
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)