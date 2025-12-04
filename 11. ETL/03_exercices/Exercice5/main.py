# ## Exercice 5 - API Météo

# **Objectif** : Récupérer et comparer la météo de plusieurs villes

# **Prérequis** : Compte OpenWeatherMap avec API key

# **Tâches**
# 1. Définir une liste de 10 villes françaises
# 2. Pour chaque ville, récupérer :
#    - Température actuelle
#    - Température ressentie
#    - Humidité
#    - Description
# 3. Créer un DataFrame avec ces informations
# 4. Identifier la ville la plus chaude et la plus froide
# 5. Calculer la température moyenne
# 6. Sauvegarder dans `meteo_villes.csv`
# 7. **Bonus** : Ajouter une gestion d'erreur si une ville n'est pas trouvée

import requests
import pandas as pd

cities = ['Lille', 'Lyon', 'Bordeaux', 'Marseille', 'Rouen', 'Amiens','Paris','Dijon','Saint Omer']

API_KEY = "b90ad04ddaf256f1a67f07cc2ce17c67"
BASE_URL = 'https://api.openweathermap.org/data/2.5'


url = f'{BASE_URL}/weather'

data_list = []
for city in cities:
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'fr'
    }

    response = requests.get(url, params=params)
    data = response.json()

    data_list.append({
        'city': data['name'],
        'temperature': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    })


df = pd.DataFrame(data_list)
print(df)

temp_cities = df['temperature'].sort_values(ascending=False)
avg_temp = df['temperature'].mean()
print(avg_temp)


with pd.ExcelWriter('meteo_villes.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='data', index=False)
    temp_cities.to_excel(writer, sheet_name='trier par temperature', index=False)
    avg_temp.to_excel(writer, sheet_name='temperature moyenne', index=False)
