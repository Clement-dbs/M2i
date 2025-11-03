# ---------------------------------------------------------------------
# Les Tuples (`tuple`)
# ---------------------------------------------------------------------

# Un tuple est une collection ordonnée mais IMMUTABLE

# Déclaration classique avec des parenthèses
couleurs = ("Rouge", "Vert", "Bleu", "Jaune", "Noir")

# Déclaration sans parenthèses (Python comprend automatiquement que c'est un tuple)
animaux = "Chat", "Chien", "Oiseau"

# Tuple avec un seul élément (attention à la virgule !)
mon_tuple = ("Unique",)  # Correct
autre_tuple = "Seul",    # Correct
tuple_faux = ("Unique")  # Faux (Python considère que c'est une **chaîne de caractères**)

# Vérification des types
print(type(couleurs))  # <class 'tuple'>
print(type(animaux))   # <class 'tuple'>
print(type(mon_tuple)) # <class 'tuple'>
print(type(tuple_faux)) # <class 'str'> (Erreur classique)

# Accès aux éléments d'un tuple avec index positif et négatif

print(couleurs[0])  # "Rouge" (1er élément)
print(couleurs[-1])  # "Noir" (dernier élément)

# Extraction d’une sous-partie avec slicing
print(couleurs[1:4])  # ('Vert', 'Bleu', 'Jaune')

# Vérifier la présence d'un élément
if "Vert" in couleurs:
    print("Le Vert est dans le tuple")

# Utilisation de `.index(element)` pour trouver la position d'un élément

# `.index(element)` retourne l'index de la première occurrence d'un élément dans le tuple
index_bleu = couleurs.index("Bleu")
print("Index de 'Bleu' :", index_bleu)  # Affiche 2


# Si l'élément n'est pas trouvé, `.index()` renvoie une erreur :
# index_non_existant = couleurs.index("Rose")  # ValueError: tuple.index(x): x not in tuple

# Retour multiple d'une fonction (Python retourne un tuple)

# Une fonction peut retourner **plusieurs valeurs**, sous forme d'un **tuple**.

def calculs(a, b):
    somme = a + b
    produit = a * b
    return somme, produit  # Python retourne un tuple

# Récupération des valeurs retournées
resultat = calculs(4, 5)
print("Retour de la fonction :", resultat)  # (9, 20)

# Décomposition du tuple en plusieurs variables
somme_result, produit_result = calculs(4, 5)
print("Somme :", somme_result)  # 9
print("Produit :", produit_result)  # 20

var1, _,_,var2 = (2,4,"toto",True)
print(var1)
print(var2)

# Convertir un tuple en liste pour modification

couleurs_liste = list(couleurs)  # Conversion en liste
couleurs_liste.append("Blanc")   # Modification possible
couleurs = tuple(couleurs_liste)  # Conversion en tuple à nouveau
print("Tuple modifié :", couleurs)