def addition(*args):
    print("args contient :", args)
    print("Type de args :", type(args))
    print("Somme =", sum(args))

# Appel avec différents nombres d'arguments
addition(1, 2, 3)
addition(10, 20)

def afficher_infos(**kwargs):
    print("kwargs contient :", kwargs)
    print("Type de kwargs :", type(kwargs))

    for cle, valeur in kwargs.items():
        print(f"{cle} : {valeur}")

# Appel avec des paires clé=valeur
afficher_infos(nom="Alice", age=25, ville="Paris")

def demo_combinee(prenom, *args, **kwargs):
    print("Prenom :", prenom)
    print("Autres args :", args)
    print("Kwargs :", kwargs)

demo_combinee("Bob", 1, 2, 3, age=30, ville="Lyon")