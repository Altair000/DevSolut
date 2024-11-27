import requests

def get_fake_data(country_code):
    response = requests.get(f'https://randomuser.me/api/?nat={country_code}')
    return response.json()