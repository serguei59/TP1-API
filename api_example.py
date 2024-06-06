import requests

api_key = '4a7830559ab8bcc5272dfc0ecfb2db8d'
city = 'Paris'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erreur:', response.status_code)