import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# - Configurer des tentatives automatiques (retries) en cas d'erreur HTTP
#   ou de code de statut considéré comme "transient" (503, 500, etc.).
# - Utiliser une Session requests configurée avec un HTTPAdapter + Retry.

# Configuration de la stratégie de retry.
retry_strategy = Retry(
    total=5,                    # Nombre total de tentatives (1 initiale + 2 retries)
    backoff_factor=1,           # Délai exponentiel entre les tentatives : # 1s, 2s, 4s, ...
    status_forcelist=[429, 500, 502, 503, 504],  # Codes HTTP pour lesquels on retry
    allowed_methods=["GET", "POST"]              # Méthodes HTTP concernées
)

# Création d'un adapter HTTP avec la stratégie de retry.
adapter = HTTPAdapter(max_retries=retry_strategy)

# Création d'une Session requests.
# Une Session :
# - réutilise les connexions HTTP
# - permet de configurer des paramètres communs (headers, retries, etc.)
session = requests.Session()

# On "monte" l'adapter sur les schémas http et https.
session.mount("http://", adapter)
session.mount("https://", adapter)

# URL qui renvoie un code 500 pour déclencher des retries (httpbin local).
url = "http://localhost:8080/status/429" # avec container httpbin


try:
    # Appel via la session, avec un timeout.
    response = session.get(url, timeout=5)

    # Si malgré les retries le code est encore dans les 4xx/5xx, raise_for_status()
    # lèvera une exception HTTPError.
    response.raise_for_status()

    data = response.json()
    print("Données reçues :", data)

except requests.exceptions.RequestException as e:
    # Cette exception englobera les erreurs après toutes les tentatives.
    print(f"Échec après les tentatives configurées : {e}")