# Le bloc try permet de tester notre code afin de récupérer les éventuelles exceptions
try:
    age = int(input("Saisir votre age : ")) # Si la saisie de l'utilisateur est un str alors une exception est levé
    print(f"L'age saisie est {age}.")
except: # Le bloc except permet de récupérer une exception (implicitement la classe Exception)
    print("Saisie invalide !")
finally: # Le bloc finally permet d'executer un bloc de code que l'on lève une exception ou non.
    print("Fin du test")


try:
    age = int(input("Saisir votre age : "))
    if age < 0 or age > 120:
        # Pour lever une exception, on doit utiliser le mot-clé 'raise' suivit de l'exception souhaité.
        raise Exception("Erreur lors de la saisie d'age") 
except ValueError: 
    print("Saisie invalide !")
except Exception as e: # Pour afficher le message de l'exception, il nous faut d'abord la récupérer avec 'as'
    print("Une autre exception à été levée")
    print(e)
else: # Le bloc else est executé si aucune exception n'a été levée
    print("La saisie c'est bien passé")
finally:
    print("Fin du test")

# Pour créer une exception personnalisé, nous devons créer une classe qui hérite d'Exception
class AgeException(Exception):
    # On peut ajouter des attributs supplémentaire si l'on souhaite détaillé nos messages d'erreur.
    def __init__(self, age, message):
        self.message = message
        self.age = age

def input_age():
    age = int(input("Saisir votre age : "))
    if age < 0 or age > 120:
        raise AgeException(age, "Erreur lors de la saisie d'age.")

    if age % 2 == 0: 
        raise ValueError("L'age est pair")

try:
    input_age()
except AgeException as e:
    print("Age invalide !")
    print(e)
except Exception:
    print("Saisie invalide !")
finally:
    print("Fin du test")
