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

#requete2()

def requete2_Celsius():
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
        print(f"Température: {main['temp']-273.15}°C")
        print(f"Pression: {main['pressure']} hPa")
        print(f"Humidité: {main['humidity']}%")
        print(f"Vitesse du vent: {wind['speed']} m/s")
        print(f"Description: {weather['description']}")
    else:
        print('Erreur:', response.status_code)

#requete2_Celsius()

def requete1_post():
    url = 'https://jsonplaceholder.typicode.com/posts'
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = requests.post(url, json=payload)
    if response.status_code == 201:
        print('Données envoyées avec succès:', response.json())
    else:
        print('Erreur:', response.status_code)

#requete1_post()

def requete2_post():
    url = 'https://jsonplaceholder.typicode.com/posts'
    

    response = requests.post(url)
    if response.status_code == 201:
        print('Données envoyées avec succès:', response.json())
    else:
        print('Erreur:', response.status_code)

#requete2_post()

def requete_erreur1():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    # executer la clause try (ce qui est entre try et except)
    try:
        #
        response = requests.get(url)
        #
        response.raise_for_status()
        #
        data = response.json()
        print(data)
    # si aucune exception n est levée 
    except requests.exceptions.HTTPError as err:
        print(f'Erreur HTTP: {err}')
    except requests.exceptions.RequestException as err:
        print(f'Erreur de requête: {err}')

requete_erreur1()









