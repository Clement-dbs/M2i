
2. **Création d'un container Alpine :**

   - Utilisez la commande Docker pour créer un container basé sur l'image Alpine.
   - Connectez-vous au shell du container nouvellement créé.

```bash
docker pull alpine
docker run -it --name my-alpine alpine # Si l'on ne possède pas l'image, docker va automatiquement la chercher sur github. 
```

3. **Récupération d'un dépôt GitHub :**

   - À l'intérieur du container, utilisez la commande `git` pour cloner un dépôt public depuis GitHub (par exemple, https://github.com/votre-utilisateur/exemple-repo.git).
   - Allez dans le répertoire du dépôt cloné.

```bash
apk update 
apk upgrade 
apk add git
apk add nano
cd /home
git clone https://github.com/LoickUtopios/DataAnalsyt.git
```

4. **Modification du contenu :**
   - À l'intérieur du container, ouvrez un fichier texte (par exemple, README.md) à l'aide d'un éditeur de texte disponible dans l'image Alpine.
   - Ajoutez une ligne de texte à votre choix et enregistrez le fichier.


```bash
nano file.txt
git add .
git commit -m "Modification de file"

# Si l'on souhaite push depuis docker
git remote set-url origin https://LoickUtopios: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@github.com/LoickUtopios/DataAnalsyt.git

git remote set-url origin https://nom_user:token@github.com/nom_user/nom_repo.git
```
