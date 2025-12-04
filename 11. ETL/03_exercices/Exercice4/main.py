# ## Exercice 4 - REST Countries


# **Objectif** : Analyser les données des pays

# **Tâches**
# 1. Récupérer tous les pays d'Europe
# 2. Créer un DataFrame avec : nom, capitale, population, superficie
# 3. Calculer la densité de population (population / superficie)
# 4. Identifier les 5 pays les plus peuplés d'Europe
# 5. Calculer la population totale de l'Europe
# 6. Trouver le pays avec la plus grande densité
# 7. Sauvegarder les résultats dans `pays_europe.xlsx`

# **API** : `https://restcountries.com/v3.1`

import requests
import pandas as pd
import openpyxl

# 1. Récupérer tous les pays d'Europe
countries = requests.get('https://restcountries.com/v3.1/region/europe?fields=name,capital,population,area')

if countries.status_code == 200:
    result = countries.json()
    # 2. Créer un DataFrame avec : nom, capitale, population, superficie
    df = pd.DataFrame(result)
    df = df[['name', 'capital','area','population']]

    # 3. Calculer la densité de population (population / superficie)
    df['density_pop'] = df['population'] / df['area'] 
    print(df['density_pop'])

    # 4. Identifier les 5 pays les plus peuplés d'Europe
    country_most_lived = df.sort_values(by="population", ascending=False)[:5]
    print(f"les 5 pays les plus peuplés d'Europe : {country_most_lived}")

    # 5. Calculer la population totale de l'Europe
    df['sum_pop_europe'] = df['population'].sum()
    print(f"La population totale de l'Europe : {df['sum_pop_europe']}")

    # 6. Trouver le pays avec la plus grande densité
    country_most_density = df.sort_values(by='density_pop', ascending=False)[:1]
    print(f"le pays avec la plus grande densité{country_most_density}")

    # 7. Sauvegarder les résultats dans `pays_europe.xlsx


    with pd.ExcelWriter('pays_europe.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='data', index=False)
        df['density_pop'].to_excel(writer, sheet_name='La densité de population', index=False)
        country_most_lived.to_excel(writer, sheet_name='Les 5 pays les plus peuplés d\'Europe', index=False)
        df['sum_pop_europe'].to_excel(writer, sheet_name='La population totale de l\'Europe', index=False)
        country_most_density.to_excel(writer, sheet_name='Le pays avec la plus grande densité', index=False)
