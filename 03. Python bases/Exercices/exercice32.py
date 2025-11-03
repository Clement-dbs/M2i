# Exercice :
# Écrire un algorithme permettant de saisir 15 notes et de les afficher.
# Vous pouvez utiliser une boucle pour demander à l'utilisateur de saisir les notes,
# puis les afficher une fois toutes saisies.


# Correction 1
print("Solution 1 :")
print() # saut de ligne 

# Initialisation d'une liste vide pour stocker les notes
notes = []

# Boucle pour saisir 15 notes
for i in range(5):
    note = float(input(f"Saisissez la note {i + 1} : "))  # Demande une note (nombre réel)
    notes.append(note)  # Ajoute la note à la liste

# Affichage des notes saisies
print("\nNotes saisies :")
for i, note in enumerate(notes, start=1):
    print(f"Note {i} : {note}")

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne

# Initialisation d'une liste vide
notes = []

# Compteur pour suivre le nombre de notes saisies
i = 0

# Boucle pour saisir 15 notes
while i < 15:
    note = float(input(f"Saisissez la note {i + 1} : "))
    notes.append(note)  # Ajout à la liste
    i += 1  # Incrémentation du compteur

# Affichage des notes saisies
print("\nNotes saisies :", notes)