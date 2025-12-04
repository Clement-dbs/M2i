# ## Exercice 3 - GET avec JSONPlaceholder


# **Objectif** : Récupérer et analyser des données

# **Tâches**

# 1. Récupérer tous les utilisateurs (`/users`)
# 2. Afficher le nom et l'email de chaque utilisateur
# 3. Récupérer tous les posts de l'utilisateur avec `userId=1`
# 4. Compter combien de posts chaque utilisateur a créé
# 5. Récupérer les commentaires du post `id=1`
# 6. Créer un DataFrame Pandas avec :
#    - Colonnes : post_id, post_title, nombre_commentaires
#    - Pour les 10 premiers posts

# **Astuce** : Utiliser des boucles et `pd.DataFrame()`


import requests
import pandas as pd

# 1. Récupérer tous les utilisateurs (`/users`)
response = requests.get("https://jsonplaceholder.typicode.com/users")
if response.status_code == 200:
    users = response.json()
    print(users)

# 2. Afficher le nom et l'email de chaque utilisateur
if response.status_code == 200:
    users = response.json()
    for user in users:
        print(f"Nom: {user['name']}, Email: {user['email']}")
    
# 3. Récupérer tous les posts de l'utilisateur avec `userId=1`   
response_posts = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 1})
if response_posts.status_code == 200:
    posts_user_1 = response_posts.json()
    print(f"Les posts pour l'utilisateur 1: {posts_user_1}")

# 4. Compter combien de posts chaque utilisateur a créé

for user in users:
    response_user_posts = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": user['id']})
    if response_user_posts.status_code == 200:
        user_posts = response_user_posts.json()
        print(f"Utilisateur {user['id']} à créér {len(user_posts)} posts")
        
    

# 5. Récupérer les commentaires du post `id=1`
comments = response_posts = requests.get("https://jsonplaceholder.typicode.com/comments", params={"id": 1})
if comments.status_code == 200:
    post_comments = comments.json()
    print(f"Commentaires pour le post 1: {post_comments}")

# 6. Créer un DataFrame Pandas avec :
#    - Colonnes : post_id, post_title, nombre_commentaires
#    - Pour les 10 premiers posts


response_posts = requests.get("https://jsonplaceholder.typicode.com/posts", params={'id' : range(1,11)})
if response_posts.status_code == 200:
    posts = response_posts.json()
    df = pd.DataFrame(posts)
    df = df[['id', 'title']]



print(df)




