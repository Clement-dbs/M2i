git init

# Ajouter une connexion avec un repot distant 
git remote add origin https://votre-repo.git

# Vérifier les remote en cours 
git remote

# Après modification, nous pouvons transmettre les informations sur le repot distant
git push origin main

# Pour récupérer les données du repo distant
git fetch origin main
git merge origin/main # (à partir de main)

git pull origin main 

# Pour récupérer un projet déjà existant sur le repot distant
git clone https://votre-repo.git
