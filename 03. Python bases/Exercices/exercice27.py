# Exercice :
# Écrire la fonction "soustraire" qui prend en paramètre :
# - nombre a
# - nombre b
# Elle retournera un entier qui sera la soustraction de ces deux nombres.
# Exemple : soustraire(2, 1) # résultat = 1.
# De plus, lors de l'exécution, la fonction affichera "Je soustrais 2 et 1".
# Vous afficherez le résultat à l'aide de la fonction print().

# Correction 1
print("Solution 1 :")
print() # saut de ligne 

def soustraire(a, b):
    """Retourne la soustraction de a et b et affiche l'opération."""
    print(f"Je soustrais {a} et {b}")
    return a - b

# Test de la fonction
resultat = soustraire(3, 1)
print(f"Résultat : {resultat}")  # Affiche "Résultat : 1"

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

def soustraire_defaut(a: int = 0, b: int = 0) -> int:
    print(f"Je soustrait {a} et {b}")
    return a - b

# Test de la fonction
resultat = soustraire_defaut(2, 1)
print(f"Résultat : {resultat}")  # Affiche "Résultat : 1"

# Correction 3
print() # saut de ligne 
print("Solution 3 :")
print() # saut de ligne 

soustraire_lambda = lambda a, b: print(f"Je soustrais {a} et {b}") or (a - b)

# Test de la fonction
resultat = soustraire_lambda(1, 1)
print(f"Résultat : {resultat}")
