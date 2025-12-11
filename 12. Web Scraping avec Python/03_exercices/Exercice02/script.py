from bs4 import BeautifulSoup
import requests

URL = "http://quotes.toscrape.com"
request = requests.get(URL)

soup = BeautifulSoup(request.text,'lxml')

# **Tâches**
# 1. Récupérer la page d'accueil
# 2. Parser avec BeautifulSoup
# 3. Trouver toutes les citations (class="quote")
# 4. Pour chaque citation, extraire :
#    - Le texte de la citation
#    - L'auteur
#    - Les tags
# 5. Afficher les 5 premières citations
# 6. Compter le nombre total de citations sur la page
# 7. Créer une liste de dictionnaires avec les données
# 8. **Bonus** : Sauvegarder dans un fichier JSON



divs = soup.find_all("div", class_="quote",limit=5)

list_quotes = []
for div in divs:
    text = div.find("span", class_="text").get_text()
    author = div.find("small", class_="author").get_text()
    tags = [tag.text for tag in div.find_all("a", class_="tag")]
    
    list_quotes.append({
        'text': text,
        'author': author,
        'tags': tags
    })




for quote in list_quotes:
    print(quote)


# # # 6. Compter le nombre total de citations sur la page
# divs = soup.find_all("div", class_="quote")

# list_quotes = []
# for div in divs:
#     text = div.find("span", class_="text").get_text()
#     author = div.find("small", class_="author").get_text()
#     tags = div.find("a", class_="tag")
#     list_quotes.append([text,author,tags])
#     print(text)
#     print(author)
#     print(tags)

# print(f"Nombre total de citations sur la page : {len(list_quotes)}")
 



    


