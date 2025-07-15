import requests

BASE_URL = 'https://the-one-api.dev/v2'
TOKEN = 'WyP-kbOZiDH3F-trJMxG'
HEADERS = {
    'Authorization':f'Bearer {TOKEN}'
}

url = f'{BASE_URL}/movie'

response = requests.get(url, headers=HEADERS)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")
