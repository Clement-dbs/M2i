from abc import ABC, abstractmethod

# Pour créer une classe abstraite/interface, il nous faut hériter de la classe ABC du module abc
#
# Toutes les classes qui hériterons de la classe abstraite seront obligé de définir les méthodes abstraites.
class Dinosaure(ABC):

    # Nous pouvons définir un constructeur dans la classe abstraite pour obtenir des attibuts de bases
    # mais elle ne sera pas utilisé directement, uniquement par ses enfants.
    def __init__(self, couleur, nom):
        self.couleur = couleur
        self.nom = nom

    # Une classe abstraite peut définir des méthodes d'instances afin que tout ses enfants la possède
    def manger(self):
        print("Miamm")

    # Cette méthode abstraite n'ont pas besoin de corps, vu que leur but n'est pas d'être utilisé dans cette classe
    # Cependant, elle devra être redéfinit dans les classes enfants. 
    @abstractmethod
    def crier(self):
        pass

# En héritant de notre classe abtraite, on est forcé d'implémenter les méthodes abtraites de celle-ci
class Raptor(Dinosaure):

    def __init__(self, couleur, nom, plume):
        super().__init__(couleur, nom)
        self.plume = plume
    
    # Je peut, comme pour un héritage standard, reféfinir les méthodes d'instances (non-obligatoire)
    def manger(self):
        super().manger()
        print("MiamMiam")

    # Nous devons redéfinir cette méthode abstraite sous peine d'avoir une exception
    def crier(self):
        print("Warrr") 


# dinosaure = Dinosaure("vert", "Stego") # ERREUR car la classe Dinosaure est abtraite.

raptor = Raptor("vert", "Raptor", "48") # Si on ne reféfinit pas crier, la classe Raptor ne pourra pas être instanciée.
raptor.crier()
raptor.manger()