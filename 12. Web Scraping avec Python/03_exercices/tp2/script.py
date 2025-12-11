# ## TP 2 - Scraper multi-pages

# **Objectif** : Scraper plusieurs pages avec pagination

# **Site** : http://quotes.toscrape.com

# **Mission**
# Créer un scraper complet qui :
# 1. Détecte automatiquement le nombre de pages
# 2. Scrape toutes les pages (jusqu'à 10 max)
# 3. Pour chaque citation, extrait :
#    - Texte
#    - Auteur
#    - Tags
#    - URL de l'auteur
# 4. Créer un fichier Excel avec 3 feuilles :
#    - "Citations" : Toutes les citations
#    - "Auteurs" : Liste unique des auteurs avec nb de citations
#    - "Tags" : Liste des tags avec fréquence
# 5. Génère des statistiques :
#    - Top 5 auteurs les plus cités
#    - Top 10 tags les plus utilisés
#    - Longueur moyenne des citations

# **Contraintes**
# - Code modulaire (fonctions)
# - Gestion d'erreurs complète
# - Logging
# - Respect du délai entre requêtes

from bs4 import BeautifulSoup
import requests
import pandas as pd

BASE_URL = 'http://quotes.toscrape.com'
list_quotes = []

def is_next_page(num_page):

    home_page = requests.get(f"{BASE_URL}/page/{num_page}")
    reponse = home_page.text
    soup = BeautifulSoup(reponse, 'lxml')
    try:
        return soup.find("nav").find("ul", class_="pager").find("li", class_="next").find("a")['href']
    except Exception as e:
        print(f"No more page to scrap, error : {e}")
        return False

def get_quotes(num_page):
    home_page = requests.get(f"{BASE_URL}/page/{num_page}")
    reponse = home_page.text
    soup = BeautifulSoup(reponse, 'lxml')

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small").get_text()
        author_url = quote.find("a")['href']
        tag = [tag.text for tag in quote.find_all("a",class_="tag")]
        
        list_quotes.append({
        'text': text,
        'author':author,
        'author_url': author_url,
        'tag': tag
        })
    return list_quotes

i = 1
while True:
    get_quotes(i)
    print(list_quotes)
    if is_next_page(i):
        i = i + 1
        continue
    else:
        break
    

df = pd.DataFrame(list_quotes)

df_quotes = df["text"]
df_author = df.groupby("author").size().sort_values(ascending=False)


with pd.ExcelWriter("rapport.xlsx") as writer:
    df_quotes.to_excel(writer, sheet_name="citations", index=False)
    df_author.to_excel(writer, sheet_name="auteurs", index=False)


print(df)

avg_quote_len = ''
df.to_csv("quotes.csv")


