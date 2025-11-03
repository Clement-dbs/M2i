# EXercice 15

mois = int(input("Saisir un numéro de mois : "))

if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
    print("31 jours")
elif mois == 4 or mois == 6 or mois == 9 or mois == 11:
    print ("30 jours")
elif mois == 2:
    print("28 ou 29 jours")
else:
    print("Numero de mois invalide")

match mois:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 jours")
    case 4 | 6 | 9 | 11 :
        print("30 jours")
    case 2:
        print("28 ou 29 jours")
    case _:
        print("Numero de mois invalide")