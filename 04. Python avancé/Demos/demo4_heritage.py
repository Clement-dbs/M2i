class Canide:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Le canidé fait un bruit !")

canide = Canide("Poomba", 5)
# print(canide) # Fonctionne car __str__ est hérité de la classe object

# Si l'on voit que des attributs/méthodes sont communs entre plusieurs classes
# il n'y a pas besoin de les réécrire, il suffit d'hériter d'une classe plus général contenant la partie commune.
class Loup(Canide):
    # Si aucun constructeur n'a été définit, nous récupérons le constructeur du parent

    # Si l'on définit un constructeur, il remplacera celui du parent
    # On pourra ajouter des attributs supplémentaire.
    def __init__(self, name, age, race):
        super().__init__(name, age) # On appel le constructeur du parent avec ses paramètres avant d'ajouter de nouveaux attributs.
        self.race = race

    # Ici, on remplace le make_sound() du parent, on appelle ça la rédéfinition (overide)
    def make_sound(self):
        super().make_sound() # On appel d'abord le comportement du parent avant d'ajouter des spécificités
        print("Le loup fait 'Woouuu!!'")

class Chien(Canide):
    
    def make_sound(self):
        super().make_sound() # On appel d'abord le comportement du parent avant d'ajouter des spécificités
        print("Le Chien fait 'Waff !!'")


loup = Loup("Balto", 10, "Loup blanc")
loup.make_sound() # Il fera appel à la méthode de sa classe

list_canide = [Canide("Gloups", 5), Chien("Rex", 4), Loup("Balto", 4, "Loup gris")]

for canide in list_canide: 
    canide.make_sound()