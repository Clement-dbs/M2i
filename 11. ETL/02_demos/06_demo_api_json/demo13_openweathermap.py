import requests
import os
from dotenv import load_dotenv


load_dotenv()

# Récupération de la clé d'API depuis les variables d'environnement.
# Cela évite de mettre la clé en dur dans le code.
API_KEY = os.getenv('OPENWEATHER_API_KEY')

# URL de base de l'API OpenWeather (version "Current Weather Data").
BASE_URL = 'https://api.openweathermap.org/data/2.5'

# Ville pour laquelle on souhaite la météo.
ville = 'Tourcoing'

# Construction de l'URL complète pour la météo actuelle.
url = f'{BASE_URL}/weather'

# Paramètres de la requête :
# - q      : nom de la ville
# - appid  : clé d'API
# - units  : "metric" pour avoir la température en °C
# - lang   : "fr" pour avoir les descriptions en français
params = {
    'q': ville,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'fr'
}

# Appel HTTP GET vers l'API.
response = requests.get(url, params=params)

# Conversion de la réponse en JSON.
data = response.json()
print(data)

print(f"Météo à {ville} :")
print(f"Température : {data['main']['temp']}°C")
print(f"Ressenti : {data['main']['feels_like']}°C")
print(f"Description : {data['weather'][0]['description']}")
print(f"Humidité : {data['main']['humidity']}%")