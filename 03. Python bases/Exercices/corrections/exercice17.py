# Exercice 17

caractere = input("saisir un caractere : ")

if caractere.isalpha():
    print(f"{caractere} est une lettre")
elif caractere.isdigit():
    print(f"{caractere} est une chiffre")
else:
    print(f"{caractere} est un caractere spécial")