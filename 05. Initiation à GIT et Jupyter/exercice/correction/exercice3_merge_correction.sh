1. Créer un nouveau repository Git
git init

2. Ajouter un fichier et le commiter `(C1)`
echo "Ajout fichier 1" > fichier.txt
git add fichier.txt
git commit -m "Ajout du fichier 1"

3. Modifier la première ligne du fichier et commiter `(C2)`
echo "Fichier 1 modifié" > fichier.txt
git commit -am "Modification du fichier 1"
git log --oneline

4. Créer une feature branch `B1` à partir de `C1`
git checkout 9431163
git branch feature
git switch feature

5. Faire une modification de la première ligne du fichier et commiter `(C3)`
echo "Modification par feature" > fichier.txt
git commit -am "Modification par feature"

6. Merger `B1` dans `main` en résolvant les conflits
git switch main
git merge feature
git status
git add fichier.txt
git commit -m "Merge de feature - conflit resolue"
git log --oneline --all --graph