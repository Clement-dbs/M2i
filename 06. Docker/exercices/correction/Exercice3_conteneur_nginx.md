
2. **Recherche d'une image sur le hub Docker :**

   - Rechercher l' image nginx sur le hub Docker.Par exemple, recherchons une image "nginx" :

```bash
docker search nginx
```

3. **Téléchargement d'une image :**

   - téléchargez l'image nginx sur votre machine.

```bash
docker pull nginx
```

4. **Exécution d'un conteneur :**

   - Exécutez un conteneur basé sur l'image que vous avez téléchargée.
     Démarrer un conteneur détaché, expose le port 80 du conteneur sur le port 8080 de votre machine, et donne un nom au conteneur.

```bash
docker run --name my-nginx -p 8080:80 -d nginx
```

5. **Vérification du conteneur en cours d'exécution :**

   - Avec une commande vérifiez que le conteneur est en cours d'exécution.

   - Ouvrez un navigateur web et accédez à `http://localhost:8080` pour voir si la page d'accueil de Nginx s'affiche.


```bash
docker ps
```

6. **Exploration du conteneur :**

   - Utilisez une commande pour accéder à une session interactive à l'intérieur du conteneur.
   - Explorez le système de fichiers à l'intérieur du conteneur.
   - Modifier la page index.html su serveur nginx.

   Note : le gestionnaire de package sur nginx est apt

```bash
docker exec -it my-nginx bash

apt upgrade
apt update
apt install nano
nano /usr/share/nginx/html/index.html
```

7. **Arrêt et suppression du conteneur :**
   - Arrêtez le conteneur.
   - Supprimez le conteneur.

Cet exercice devrait vous donner une idée de base de la création, de l'exécution, et de l'exploration de conteneurs Docker sans se concentrer sur les Dockerfiles ou Docker Compose.
  
```bash
docker stop my-nginx
docker rm my-nginx
```