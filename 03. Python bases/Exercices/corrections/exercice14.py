# Exercice 14

jour = int(input("Saisir un jour de la semaine :"))

if jour == 1:
    print("Lundi")
elif jour == 2:
    print("Mardi")
elif jour == 3:
    print("Mercredi")
elif jour == 4:
    print("Jeudi")
elif jour == 5:
    print("Vendredi")
elif jour == 6:
    print("samedi")
elif jour == 7:
    print("dimanche")
else:
    print("Numero invalide")

match jour:
    case 3:
        print("Mercredi")
    case 1:
        print("Lundi")
    case 2:
        print("Mardi")
    case 4:
        print("Jeudi")
    case 5:
        print("Vendredi")
    case 6:
        print("Samedi")
    case 7:
        print("Dimanche")
    case _:
        print("Numero invalide")