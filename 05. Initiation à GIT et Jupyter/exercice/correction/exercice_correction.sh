git init

echo "Du texte" > fichier1.txt
git add fichier1.txt
git commit -m "Ajout du fichier1"

echo "Modification" >> fichier1.txt
git commit -am "Modification de fichier1"

git log