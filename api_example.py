import requests

""" api_key = '4a7830559ab8bcc5272dfc0ecfb2db8d'
city = 'Paris'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erreur:', response.status_code) """

def requete1():
    api_key = '4a7830559ab8bcc5272dfc0ecfb2db8d'
    city = 'Paris'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print('Erreur:', response.status_code)
    
#requete1()

def requete2():
    api_key = '4a7830559ab8bcc5272dfc0ecfb2db8d'
    city = 'Paris'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]

        
        print(f"Ville: {city}")
        print(f"Température: {main['temp']}°K")
        print(f"Pression: {main['pressure']} hPa")
        print(f"Humidité: {main['humidity']}%")
        print(f"Vitesse du vent: {wind['speed']} m/s")
        print(f"Description: {weather['description']}")
    else:
        print('Erreur:', response.status_code)

requete2()


