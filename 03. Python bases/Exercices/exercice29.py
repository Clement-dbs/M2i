# Exercice :
# Écrire une fonction compter_lettre_a.
# Cette fonction prendra en paramètre une chaîne.
# Créer une boucle qui parcourt les lettres de la chaîne et compte le
# nombre de lettres égales à "a".
# La fonction renverra un entier.
# Exemple : compter_lettre_a("abba") # résultat : 2
# Exemple : compter_lettre_a("mixer") # résultat : 0
#
# Écrire une autre fonction sans boucle qui utilisera count à la place.

# Correction 1
print("Solution 1 :")
print() # saut de ligne 

def compter_lettre_a(chaine):
    """Compte le nombre de lettres 'a' dans la chaîne en utilisant une boucle."""
    compteur = 0
    for lettre in chaine:
        if lettre == "a":
            compteur += 1
    return compteur

# Tests de la fonction
print(compter_lettre_a("abba"))   # Résultat : 2
print(compter_lettre_a("mixer"))  # Résultat : 0


# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

def compter_lettre_a_count(chaine):
    """Compte le nombre de lettres 'a' dans la chaîne en utilisant count()."""
    return chaine.count("a")

# Tests de la fonction
print(compter_lettre_a_count("abba"))   # Résultat : 2
print(compter_lettre_a_count("mixer"))  # Résultat : 0


# Correction 3
print("Solution 3 :")
print() # saut de ligne 

def compter_lettre(chaine,l="a"):
    """Compte le nombre de lettres 'a' dans la chaîne en utilisant une boucle."""
    compteur = 0
    for lettre in chaine:
        if lettre == l:
            compteur += 1
    return compteur

# Tests de la fonction
print(compter_lettre("abba"))   # Résultat : 2
print(compter_lettre("mixer"))  # Résultat : 0
print(compter_lettre("mixer","i"))