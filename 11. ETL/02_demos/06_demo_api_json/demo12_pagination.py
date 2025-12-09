import requests

# - Illustrer un schéma de pagination réel avec une API publique.
# - Utiliser JSONPlaceholder et ses paramètres :
#       * _limit : nombre d'éléments par page
#       * _start : offset (position de départ)


BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def get_all_posts_paginated(page_size=20):
    """
    Récupère tous les posts de l'API JSONPlaceholder par blocs (pagination).

    Paramètres :
    - page_size : nombre d'éléments à récupérer par "page" (_limit)

    Stratégie de pagination :
    - On commence avec _start = 0
    - À chaque itération :
        * on appelle /posts?_limit=page_size&_start=start
        * si la liste renvoyée est vide → fin
        * sinon on ajoute les éléments et on augmente start de page_size
    """
    all_posts = []
    start = 0  # offset de départ

    while True:
        params = {
            "_limit": page_size,
            "_start": start
        }

        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # lève HTTPError si code 4xx / 5xx

        posts = response.json()  # doit être une liste de dicts

        # Si la page ne contient aucun élément, on s'arrête
        if not posts:
            print("Plus de données, fin de la pagination.")
            break

        # Ajout des posts récupérés à la liste globale
        all_posts.extend(posts)

        # Affichage d'information de suivi
        print(f"Page offset={start} récupérée : {len(posts)} éléments")

        # Préparer le prochain offset
        start += page_size

    return all_posts


if __name__ == "__main__":
    # Exemple : récupérer tous les posts par blocs de 25
    all_items = get_all_posts_paginated(page_size=25)
    print(f"\nNombre total de posts récupérés : {len(all_items)}")

    # Afficher quelques posts pour vérifier
    print("\nExemple des 3 premiers posts :")
    for post in all_items[:3]:
        print(f"- id={post['id']}, title={post['title']!r}")
