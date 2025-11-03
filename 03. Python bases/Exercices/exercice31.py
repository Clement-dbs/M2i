# Exercice :
# Écrire un algorithme qui déclare et stocke dans un tableau 10 chiffres,
# puis affiche le 9ème élément de la liste.

# Correction 1
print("Solution 1 :")
print() # saut de ligne 

# Déclaration d'un tableau avec 10 chiffres
tableau = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Affichage du 9ème élément (indice 8 car les indices commencent à 0)
print(f"Le 9ème élément du tableau est : {tableau[8]}")

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

# Déclaration d'un tableau avec 10 chiffres
tableau = list(range(10))  # Génère [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Affichage des éléments
print("Tableau généré :", tableau)

# Affichage du 9ème élément
print(f"Le 9ème élément est : {tableau[8]}")

# Correction 3
print() # saut de ligne 
print("Solution 3 :")
print() # saut de ligne 

import random

# Initialisation d'un tableau vide
tableau = []

# Remplissage du tableau avec 10 chiffres aléatoires entre 0 et 9
for i in range(10):
    nombre_aleatoire = random.randint(0, 99)  # Génère un chiffre aléatoire
    tableau.append(nombre_aleatoire)  # Ajoute le chiffre dans le tableau

# Affichage du tableau généré
print("Tableau généré :", tableau)

# Affichage du 9ème élément (indice 8)
print(f"Le 9ème élément du tableau est : {tableau[8]}")