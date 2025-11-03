# Exercice :
# Nous devons écrire un algorithme qui demande à l'utilisateur de
# saisir un nombre compris entre 1 et 3, et qui répète cette demande
# tant que la réponse de l'utilisateur n'est pas valide.

#nombre = int(input("Saisir un nombre entre 1 et 3 :"))

# solution 1
# boucle tant que la saisie est invalide
# while nombre < 1 or nombre > 3:
#     print("Saisie invalide. Veuillez recommencer.")
#     nombre = int(input("Saisir un nombre entre 1 et 3 :"))


# solution 2
# while not(1 <= nombre <= 3):
#     print("Saisie invalide. Veuillez recommencer.")
#     nombre = int(input("Saisir un nombre entre 1 et 3 :"))

# solution 3
while True:
    nombre = input("Saisir un nombre entre 1 et 3 :")

    if nombre.isdigit():
        nombre = int(nombre)
        if 1 <= nombre <= 3:
            break
    print("Saisie invalide. Veuillez recommencer.")



print(f"Vous avez saisie le nombre valide : {nombre}")


