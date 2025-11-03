
#fonction saluer
def saluer(nom):
    """Retourne un message de salutation avec le nom donné."""
    return f"Bonjour, {nom} !"

# fonction addition 
def addition(a, b):
    """Retourne la somme de deux nombres."""
    return a + b


if __name__ == "__main__":
    print(saluer("toto"))
    print("test addition : ",addition(3,5))
    print("Valeur de la variable __name__ dans mon_module.py : ",__name__)