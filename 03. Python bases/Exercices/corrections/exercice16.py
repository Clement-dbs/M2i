# exercice 16
annee = int(input("Saisir une annee :"))

if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print(f"{annee} est une annee bissextile")
else:
    print(f"{annee} n'est pas une annee bissextile")