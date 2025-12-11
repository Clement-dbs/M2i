# ## Exercice - Scraping de livres

# **Objectif** : Scraper un catalogue de livres

# **Site** : http://books.toscrape.com

# **Tâches**
# 1. Récupérer la page d'accueil
# 2. Pour chaque livre sur la page, extraire :
#    - Titre
#    - Prix (convertir en float)
#    - Note (étoiles → nombre)
#    - Disponibilité (In stock / Out of stock)
#    - URL de l'image
# 3. Créer un DataFrame Pandas
# 4. Calculer :
#    - Prix moyen
#    - Livre le plus cher
#    - Livre le moins cher
#    - Répartition par note
# 5. Sauvegarder dans `books.csv`
# 6. **Bonus** : Télécharger l'image du livre le plus cher

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

BASE_URL = 'http://books.toscrape.com/catalogue/page'

list_books = []

for i in range(1,51): # Scrapper plusieurs pages (ici 3)

    home_page_books = requests.get(f"{BASE_URL}-{i}.html")
    reponse = home_page_books.text
    soup = BeautifulSoup(reponse, 'lxml')
    books_section = soup.find("ol", class_='row')
    books = books_section.find_all("li")

    for book in books:

        title = book.find("h3").find("a")['title'] # titre

        price_text = book.find("div", class_="product_price").find("p", class_='price_color').get_text()
        price = float(re.findall(r"[\d.]+", price_text)[0]) # prix
        availability = book.find("div", class_="product_price").find("p", class_='instock availability').get_text(strip=True) # disponibilité

        img_url = book.find("div", class_="image_container").find("img")['src'] # url de l'image
        full_path_img = f"{BASE_URL}/{img_url}" # url entier de l'image

        list_books.append({
        'title': title,
        'price':price,
        'availability': availability,
        'note':'',
        'img_url': full_path_img
        })

# Dataframe
df = pd.DataFrame(list_books)
print(df)

avg_price =  round(df['price'].sum() / len(df['price']),2)
highest_price_book = df['price'].max()
lowest_price_book = df['price'].min()

print(f"Prix moyen : {avg_price}")
print(f"Livre le plus cher : {highest_price_book}")
print(f"Livre le moin chèr : {lowest_price_book}")

# Rapport CSV
df.to_csv('books.csv')

