# 1. Créer un nouveau repository Git
351  git init

# 2. Ajouter un fichier et le commiter `(C1)`, le modifier et le commiter `(C2)`
352  echo "Ajout fichier 1" > fichier.txt
353  git add fichier.txt
354  git commit -m "Ajout du fichier 1"
355  echo "Fichier 1 modifié" > fichier.txt
356  git commit -am "Modification du fichier 1"
357  git log --oneline
358  git switch 9431163
359  git checkout 9431163

# 3. Créer une branche `B1` à partir de `C1`
360  git branch feature
361  git switch feature

# 4. Faire une modification du fichier et commiter `C3`
362  echo "Modification par feature" > fichier.txt
363  git commit -am "Modification par feature"

# 5. Merger `B1` dans `main` de manière à avoir un historique linéaire
364  git switch main
365  git merge feature
366  git status
367  git add fichier.txt
368  git commit -m "Merge de feature - conflit resolue"
369  git log --oneline --all --graph
