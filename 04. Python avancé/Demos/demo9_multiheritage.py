class A():
    pass

class B():
    pass

class C():
    pass

class D():
    pass

class AB(A,B):
    pass

class CD(B, C, D):
    pass

class ABCD(AB, CD):
    pass

# Ici, via la méthode mro() nous récupérons l'ordre de parcours des classes parentes de la classe ABCD.
print(ABCD.mro()) # Ici -> ABCD, AB, A, C , CD, C, D

class Carnivore():
    def __init__(self, nb_dent, nb_patte):
        self.nb_dent = nb_dent
        self.nb_patte = nb_patte

    def manger(self):
        print("Je mange de la viande !")

class Plante():
    def __init__(self, couleur, longueur_tige):
        self.couleur = couleur
        self.longueur_tige = longueur_tige
        
    def manger(self):
        print("Je ne mange pas, j'ai la photosynthese !!")

# Dans le cas d'un héritage multiple, il va falloir mettres les deux classes séparé d'une virgule. 
# L'ordre précisé dans ces paranthèse va orienté l'ordre effectué par le MRO
class PlanteCarnivore(Carnivore, Plante): 
    # Si nous utilisons le mot-clé super() alors nous allons appeler le premier parents dans l'ordre du MRO
    # 
    # Si nous souhaitons utilisé une méthode ou un constructeur d'une classe en particulier alors il faut donner le nom de la classe
    # à la place du mot-clé super()
    def __init__(self, couleur, longueur_tige):
        Plante.__init__(self, couleur, longueur_tige) # Il ne faut pas oublier de passer la valeur self en premier parametre.

plante_carni = PlanteCarnivore(10, 0, "Verte", 5.0)
plante_carni.manger()