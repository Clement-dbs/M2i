import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

# - Montrer comment gérer proprement les erreurs lors d'un appel HTTP.
# - Différencier plusieurs types d'erreurs :
#       * Timeout        : le serveur met trop de temps à répondre
#       * ConnectionError: problème réseau, DNS, etc.
#       * HTTPError      : code de statut HTTP 4xx / 5xx après raise_for_status()
#       * RequestException : erreur générique de la bibliothèque requests
#       * ValueError     : problème lors du parsing JSON



try:
    # Envoi de la requête HTTP GET.
    # timeout=5 signifie : lever une exception Timeout si aucune réponse
    # n'est reçue avant 5 secondes.
    response = requests.get("http://localhost:8080/get", timeout=5)

    # raise_for_status() :
    # - Ne fait rien si le code de statut est 2xx ou 3xx
    # - Lève une exception HTTPError si le code est 4xx ou 5xx
    response.raise_for_status()

    # Tentative de parse du corps de la réponse comme JSON.
    # Si le contenu n'est pas du JSON valide, .json() peut lever ValueError.
    data = response.json()
    print("Données JSON reçues :")
    print(data)

# Timeout : le serveur a mis trop de temps à répondre.
except Timeout:
    print("Timeout : L'API met trop de temps à répondre")

# ConnectionError : problème de réseau (pas d'accès internet, DNS, etc.).
except ConnectionError:
    print("Erreur de connexion : Vérifiez votre réseau ou le serveur")

# HTTPError : erreur HTTP après raise_for_status() (404, 500, etc.).
except requests.exceptions.HTTPError as e:
    print(f"Erreur HTTP : {e}")
    # response peut contenir plus d'infos (code + corps de la réponse)
    print(f"Code : {response.status_code}")
    print(f"Message : {response.text}")

# RequestException : exception générique de requests (base pour toutes les autres).
except RequestException as e:
    print(f"Erreur générale requests : {e}")

# ValueError : problème lors du parsing JSON (réponse pas au format JSON).
except ValueError:
    print("La réponse n'est pas du JSON valide")