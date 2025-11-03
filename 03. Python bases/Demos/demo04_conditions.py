# Condition simple if

age = 17
if age >= 18: # si la condition est vraie
    print("toto")
    print("Vous etes majeur")

# avec if et else

age = 16 
if age >=18:
    print("Vous etes majeur")
else:
    print("Vous etes mineur")


# avec if, elif et else

age = 21
if age >=21:
    print("Vous etes majeur au USA")
elif age >=18:
    print("Vous etes majeur en france")
else:
    print("Vous etes mineur")

# ternaire
note = 16
resultat = "Réussi" if note >=10 else "Echec"
print(f"Resultat de l'examen {resultat}")

resultat2 = "Tres bien" if note >= 15 else "Bien" if note >=10 else "Pas bien"
print(f"Resultat de l'examen 2 {resultat2}")

if note >= 15:
    resultat2 = "Tres bien"
else:
    if note >=10:
        resultat2 = "Bien"
    else:
        resultat2 = "Pas bien"


# instruction pass
nom_utilisateur = ""
if nom_utilisateur:
    print(f"Bienvenue {nom_utilisateur}")
else:
    pass

print("Fin du programme")

voyelles = "aeiouy"
lettre = "i"
print(lettre in voyelles)
if lettre in voyelles:
    print(f"{lettre} est une voyelle")

valeur = "42"
if isinstance(valeur,int):
    print("la valeur est un int")
elif isinstance(valeur,str):
    print("la valeur est une string")

# match case
day = "luuuuuunndi"
match day:
    case "lundi":
        print("debut de la semaine")
    case "mardi":
        print("deuxieme jour")
    case "samedi" | "dimanche":
        print("c'est le week end")
    case _:
        print("Jour non reconnu")


valeur = ["42.3"]
match valeur:
    case int():
        print("nombre entier")
    case float():
        print("nombre decimal")
    case str():
        print("chaine")
    case _:
        print("inconnu")