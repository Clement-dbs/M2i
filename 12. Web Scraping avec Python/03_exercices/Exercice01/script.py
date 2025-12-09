import requests
from urllib.robotparser import RobotFileParser
from requests.exceptions import RequestException, Timeout, ConnectionError
from time import sleep
import html
import pandas as pd


BASE_URL = "http://quotes.toscrape.com"
#ROBOTS_URL = f"{BASE_URL}/robots.txt"

def home_page(url):
    try : 
        """Télécharge et affiche le contenu de robots.txt."""
        print(f"Récupération de {url} ...")
        response = requests.get(url)

        # Status HTTP (200 = OK, 404 = non trouvé, etc.)
        print("Code HTTP :", response.status_code)

        # Encoding
        print("\nEncodage détecté :", response.encoding)

        # Header
        print("\nHeader :", response.headers)
        
        # Affichage brut du fichier robots.txt
        print("\n=== Contenu de robots.txt ===")
        print(response.text[:500])
        
        # 4. Compter le nombre de caractères de chaque page
        nb_char = len(response.text)
        print(f"Nombre de caractères de la page {nb_char}")

        
        return {
            "url":url,
            "status_code":str(response.status_code),
            "text":response.text
        }
    
    except Timeout:
        print(f"Timeout pour {url}")
        
    except ConnectionError:
        print(f"Erreur de connexion pour {url}")
  
    except requests.exceptions.HTTPError:
        print(f"Erreur HTTP {response.status_code}: {url}")
 
    except RequestException as e:
        print(f"Erreur générale: {e}")


def fetch_page(url):
    sleep(1)
    full_path = f"{BASE_URL + url}"
    return home_page(full_path)
    

def save_to_html(data,page_name):
    with open(page_name, "w", encoding='UTF-8') as page:
        page.write(data['text'])

def generate_csv(data,file_name):
     with open(file_name, "w", encoding='UTF-8') as file:
        file.write(f"URL : {data['url']}\n")
        file.write(f"Status code : {data['status_code']}")
    

if __name__ == "__main__":
    
    links_list = ['love', 'inspirational', 'life']
    for link in links_list:
        request = fetch_page(f"/tag/{link}")
        save_to_html(request, f"{link}.html")
        generate_csv(request, f"rapport_{link}.csv")

       