class Gateau():

    def __init__(self, 
                 nom: str, 
                 temps_cuisson: int, 
                 liste_ingredients: list, 
                 etapes: list, 
                 nom_createur: str
                 ):
        self.__nom = nom
        self.__temps_cuisson = temps_cuisson
        self.__liste_ingredients = liste_ingredients
        self.__etapes = etapes
        self.__nom_createur = nom_createur

    def afficher_ingredient(self):
        cpt = 0
        print("=== Mes ingrédient ===")
        for ing in self.__liste_ingredients:
            cpt=cpt+1
            print(f"{cpt}. {ing}")
    
    def afficher_etapes(self):
        cpt = 0
        print("=== Mes étapes ===")
        for ing in self.__etapes:
            cpt=cpt+1
            print(f"{cpt}. {ing}")

    def afficher_recette(self):
        print("=== Ma recette ===")
        self.afficher_ingredient()
        self.afficher_etapes()

gateau = Gateau("Eclair au chocolat", 30, ["farine", "chocolat", "lait", "beurre"], ["préparer", "cuire", "servir"], "Toto")
gateau.afficher_ingredient()
gateau.afficher_recette()
