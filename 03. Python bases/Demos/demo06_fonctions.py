
# Fonction sans paramètre ni valeur de retour

def saluer():
    # Affiche un message de salutation
    print("Bonjour tout le monde !")

# Appel de la fonction
saluer()  # Affiche "Bonjour tout le monde !"

# Fonction avec paramètres

def saluer_personne(nom):
    # Affiche un message de bienvenue personnalisé avec un nom
    print(f"Bonjour, {nom} !")

# Appel de la fonction avec un argument
saluer_personne("Alice")  # Affiche "Bonjour, Alice !"
saluer_personne("Toto")

# Fonction avec retour de valeur

def addition(a, b):
    # Retourne la somme de deux nombres
    print(f"je suis dans la fonction addition et je vais renvoye {a} + {b}")
    return a + b

resultat = addition(2,3)
print(resultat)
print(addition(10,5))

# Paramètres avec valeurs par défaut

def bienvenue(nom="Invité"):
    # Affiche un message de bienvenue avec un nom par défaut
    print(f"Bienvenue, {nom} !")

bienvenue("bob")
bienvenue()

# Fonction en precisant les type des argument et de retour

def somme_nom(nom: str,nbr1: float,nbr2: int=42)-> float:
    print(f"Bonjour {nom} je fait la somme de {nbr1} et {nbr2} et vous renvoit le resultat")
    return nbr1 + nbr2

result = somme_nom("tata",23.5,65)
print(result)
result2 = somme_nom(89,32,23.5)
nom: str = "toto"
print(type(nom))
nom = 42
print(type(nom))
result = somme_nom("tutu",8)
print(result)

def greet(name: str)-> str:
    """
    Cette fonction prend un nom en entrée et affiche un message de bienvenue
    :param name:str, le nom de la personne a saluer
    :return: str , le message de bienvenue
    """
    return f"Bonjour,{name}"

print(greet("Toto"))
print(greet.__doc__)

# Fonctions anonymes Lambda

# Syntaxe d'une fonction lambda :
# lambda paramètres: expression

# Exemple classique d'une fonction normale pour additionner deux nombres :
def addition_normale(x, y):
    return x + y

# Équivalent avec une fonction lambda :
addition_lambda = lambda x, y: x + y

# Appels des fonctions
print(addition_normale(2, 3))  # Affiche 5
print(addition_lambda(2, 3))   # Affiche 5

print((lambda a, b: a * b)(3, 4))  # Affiche 12

# Autre exemple : extraction du premier caractère d'une chaîne
premier_caractere = lambda texte: texte[0]

print(premier_caractere("Python"))  # Affiche "P"