# Exercice 13

caractere = input("Sasir un caractere :").lower()

voyelles = "aeiouy"

if caractere in voyelles:
    print("Le caractère saisi est une voyelle")
else:
    print("Le caractère saisi est une consonne")

print("Le caractère saisi est une voyelle" if input("Sasir un caractere :").lower() in "aeiouy" else "Le caractère saisi est une consonne")