# Exercice :
# Écrire une fonction qui prend en paramètre :
# - prénom
# - nom
# Elle retournera une chaîne avec le prénom et le nom séparé d'un espace,
# exemple : "John Doe".
# Vous afficherez le résultat de cette fonction à l'aide de la fonction print().



# Correction 1
print("Solution 1 :")
print() # saut de ligne 

def nom_complet(prenom, nom):
    """Retourne le prénom et le nom séparés par un espace."""
    return f"{prenom} {nom}"

# Test de la fonction
print(nom_complet("John", "Doe"))  # Affiche "John Doe"

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

nom_complet_lambda = lambda prenom, nom: f"{prenom} {nom}"

# Test de la fonction
print(nom_complet_lambda("Jahn", "Doe"))

# Correction 3
print() # saut de ligne 
print("Solution 3 :")
print() # saut de ligne 

def nom_complet_defaut(prenom: str = "Jack", nom: str = "Doe") -> str:
    return prenom + " " + nom


# Test de la fonction
print(nom_complet_defaut())