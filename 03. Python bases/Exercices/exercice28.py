# Exercice :
# Écrire une fonction quelle_heure.
# Cette fonction aura un paramètre heure de type str.
# Ce paramètre aura "12h00" comme valeur par défaut.
# La fonction ne retournera aucun résultat mais affichera l'heure
# avec la fonction print().
# Exemple : quelle_heure() # résultat : "il est 12h00"
# Exemple : quelle_heure("14h00") # résultat : "il est 14h00"

# Correction 1
print("Solution 1 :")
print() # saut de ligne 

def quelle_heure(heure="12h00") -> None:
    """Affiche l'heure avec une valeur par défaut de 12h00."""
    print(f"Il est {heure}")

# Tests de la fonction
quelle_heure()        # Affiche "Il est 12h00"
quelle_heure("14h00")   # Affiche "Il est 14h00"

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

import datetime

#quelle_heure_lambda = lambda heure="12h00": print(f"Il est {heure}")
quelle_heure_lambda = lambda heure=datetime.datetime.now().time(): print(f"Il est {heure}")

# Tests de la fonction
quelle_heure_lambda()          # Affiche "Il est 12h00"
quelle_heure_lambda("14h00")   # Affiche "Il est 14h00"