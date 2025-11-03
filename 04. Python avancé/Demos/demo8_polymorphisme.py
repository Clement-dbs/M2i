class Chat():
    def miauler(self): 
        print("Miaou")

class Chaton(Chat):
    # polymorphisme par override/redéfinition
    def miauler(self):
        print("Miaou ou ?")

chat = Chat()
chaton = Chaton()
chat.miauler()
chaton.miauler()

class Canard():
    def voler(self):
        print("Le canard vole !")

    def nager(self):
        print("Le canard nage !")

class PoissonVolant():
    def voler(self):
        print("Le poisson volant vole !")

    def nager(self): 
        print("Le poisson volant nage !")
    
    def plonger(self):
        print("Le poisson volant plonge !")

class Avion():
    def voler(self):
        print("L'avion vole !!")

# Nous créeons une liste d'élément qui non aucune parenté mais qui on des méthodes en commun.
list_element = [Canard(), PoissonVolant(), Avion()]

for element in list_element:
    # En parcourant la liste de chacun des éléments, nous appelons leur méthode voler()
    # Attention, si l'un des éléments ne possèdent pas la méthode en question, nous recevrons une erreur.
    element.voler()

    # On peut vérifier si un élément est d'une certaine classe afin d'appeler ces méthodes spécifiques.
    if isinstance(element, PoissonVolant):
        element.plonger()

    # On peut également vérifier si la classe de l'élément parcourue possède une certaine méthode avant de l'utiliser.
    if "nager" in dir(element.__class__):
        element.nager()

# dir(NomClasse) permet d'afficher une liste des méthodes et attributs de classe dans la classe spécifié.
print(dir(Avion))