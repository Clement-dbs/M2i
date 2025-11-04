# Exercice 3

## Partie 1

- En utilisant votre machine Windows, lancez le service Docker, s’il n’est pas lancé.

- Créer une image Docker sur votre machine du jeu 2048.

```bash
docker search 2048
docker pull oats87/2048
```

- Vérifier que l’image est bien présente sur votre machine.

```bash
docker images
```

- Lancer ce jeu sur un port disponible au travers d’un conteneur que vous allez appeler «jeu-votre-nom ».

```bash
docker run -d -p 8080:80 --name jeu-loick oats87/2048
```

- Vérifier que le conteneur est bien lancé avec la commande adaptée.

```bash
docker ps
```

- Créer un second conteneur qui va lancer le même jeu mais avec un nom différent «jeu2-votre-nom ».

```bash
docker run -d -p 8081:80 --name jeu2-loick oats87/2048
```

- Les 2 jeux sont fonctionnels en même temps sur votre machine, effectuez la commande pour vérifier la présence des conteneurs.

```bash
docker ps
```

- Ouvrez les 2 jeux sur votre navigateur.

```bash
http://localhost:8080/
http://localhost:8081/
```

- Stopper les 2 conteneurs et assurez-vous que ces 2 conteneurs sont arrêtés.

```bash
docker stop jeu-loick
docker stop jeu2-loick
docker ps -a
```

- Relancez le conteneur «jeu2-votre-nom » et aller vérifier dans votre navigateur s’il fonctionne bien. Effectuez la commande pour voir s’il a bien été relancé. Puis stopper le.

```bash
docker start jeu2-loick
docker ps
docker stop jeu2-loick
```

- Supprimez l’image du jeu 2048 et les conteneurs associés.

```bash
docker rm jeu-loick
docker rm jeu2-loick
docker rmi oats87/2048
```

- Vérifiez que les suppressions ont bien été faite.

```bash
docker ps -a
docker images
```

## Partie 2

- Récupérer une image docker nginx.

```bash
docker pull nginx
```

- Créer un conteneur en vous basant sur cette image en lui attribuant le nom suivant : « nginx-web».

```bash
docker run -d -p 8080:80 --name nginx-web nginx
```

- Assurez-vous que l’image est bien présente et que le conteneur est bien lancé.

```bash
docker images
docker ps
```

- Ce serveur nginx web (nginx-web) devra être lancé sur un port disponible.

- Vérifier que le serveur est bien lancé au travers du navigateur.

```bash
http://localhost:8080/
```

- Une page web avec «Welcome to nignx » devrait s'afficher (voir nginx.png).

- Effectuer la commande vous permettant de rentrer à l’intérieur de votre serveur nginx.

```bash
docker exec -it nginx-web bash
```

- Une fois à l’intérieur, aller modifier la page html par défaut de votre serveur nginx en changeant le titre de la page en :  
  Welcome «votre prenom ».

```bash
apt update
apt upgrade 
apt install nano
nano /usr/share/nginx/html/index.html
```

- Relancez votre serveur et assurez-vous que le changement à bien été pris en compte, en relançant votre navigateur.

- Refaite la même opération mais en utilisant le serveur web apache et donc il faudra créer un autre conteneur.

```bash
docker search apache
docker pull httpd
docker run -d -p 8081:80 --name apache-web httpd
```

- Il faut supprimer le contenu complet de l'index.html et y mettre : "Je suis heureux et je m'appelle votre prenom".

```bash
docker exec -it apache-web bash
cd /usr/local/apache2/htdocs/
apt update
apt upgrade
apt install nano
nano index.html
```

- Le changement doit appaître dans votre navigateur.

## Partie 3

- Répétez 3 fois la même opération que pour le début de la partie 2, il faudra juste appelez vos conteneurs :

- « nginx-web3 ».

- « nginx-web4 ».

- « nginx-web5 ».

- Il faudra faire en sorte que les pages html présente dans les fichiers ci-dessous s’affiche dans chacun des navigateurs en lien avec vos conteneurs :

  -   https://target-mohamed-s3.s3.eu-west-3.amazonaws.com/html5up-editorial-m2i.zip pour nginx-web2
  -   https://target-mohamed-s3.s3.eu-west-3.amazonaws.com/html5up-massively.zip pour nginx-web3
  -   https://target-mohamed-s3.s3.eu-west-3.amazonaws.com/html5up-paradigm-shift.zip pour nginx-web4

- Stopper, ensuite, ces différents conteneurs.
