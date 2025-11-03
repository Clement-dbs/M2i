# Déclaration d'une liste
fruits = ["Pomme", "Banane", "Orange", "Mangue", "Ananas"]


# Les listes sont **indexées**, ce qui signifie que chaque élément a une position bien définie.
# En Python, les **index commencent à 0** !
# Index :       0        1         2        3         4
# Liste :  ["Pomme", "Banane", "Orange", "Mangue", "Ananas"]

# Acces aux element de ma list
print(fruits) # toutes ma liste
print(fruits[0]) # premier element
print(fruits[2]) # troisieme element

# print(fruits[99]) # IndexError: list index out of range

print(fruits[-1]) # dernier element
print(fruits[-3]) # Orange

# modification d'un element 
fruits[1] = "Fraise"
print("Après modification :", fruits) 

# Ajout d'elements
fruits.append("Cerise")  # Ajoute à la fin
fruits.insert(2, "Kiwi")  # Insère à une position spécifique
print("Après ajouts :", fruits)

# Supprimer
fruits.remove("Mangue")  # Supprime la première occurrence
print("Après suppression :", fruits)

dernier_fruit = fruits.pop()  # Supprime et retourne le dernier élément
print("Dernier élément supprimé :", dernier_fruit)
print("Après pop :", fruits)

# Extend
autres_fruits = ["Framboise", "Myrtille"]
fruits.extend(autres_fruits)  # Ajoute les éléments de `autres_fruits`
print("Après extension :", fruits)  # ['Pomme', 'Fraise', 'Kiwi', 'Orange', 'Ananas', 'Framboise', 'Myrtille']

# Count
fruits.append("Pomme")  # Ajout d'un doublon
nombre_de_pommes = fruits.count("Pomme")
print("Après ajout doublons :", fruits)
print("Nombre de 'Pomme' dans la liste :", nombre_de_pommes)  # Affiche 2
# print(fruits.count())

# Extraction d'une **sous-liste** avec le **slicing** (tranches)
print(fruits[1:4])   # Affiche ['Fraise', 'Kiwi', 'Orange']
print(fruits[:3])    # Affiche ['Pomme', 'Fraise', 'Kiwi']
print(fruits[::2])   # Affiche un élément sur deux

ma_liste = [
    1,
    2,
    3,
    'test',
    True,
    ['a', True, 25]
]

# je veux le premier element de ma_liste
print(ma_liste[0])

# je veux recuperer le numero 25 contenu dans ma seconde liste
print(ma_liste[5][2])

ma_liste = [1, 4, 5, 2, 3]
ma_liste.sort()
print(ma_liste)
ma_liste.sort(reverse=True)
print(ma_liste)

# Parcourir une liste
for fruit in fruits:
    print("Fruit :", fruit)


# Les fonctions avancees pour les listes

# `sorted()` trie une liste et retourne une **nouvelle** liste triée (sans modifier l'originale).

nombres = [5, 2, 8, 1, 9]

nombres_tries = sorted(nombres)
print("Tri croissant :", nombres_tries)  # [1, 2, 5, 8, 9]

nombres_tries_desc = sorted(nombres, reverse=True)
print("Tri décroissant :", nombres_tries_desc)  # [9, 8, 5, 2, 1]

# Tri selon une fonction personnalisée (ex: ordre des longueurs de mots)
mots = ["Python", "Java", "C", "JavaScript"]
mots_tries = sorted(mots, key=len)  # Trie par la longueur des mots
print("Tri par longueur de mot :", mots_tries) 

# filter Filtrer une liste selon une condition

nombres_pairs = list(filter(lambda x: x % 2 == 0, nombres))
print("Nombres pairs :", nombres_pairs) 

mots_filtres = list(filter(lambda mot: len(mot) > 4, mots))
print("Mots avec plus de 3 lettres :", mots_filtres) 

nombres_sup5 = list(filter(lambda x: x > 5, nombres))
print("Nombres supérieurs à 5 :", nombres_sup5)  # [8, 9]