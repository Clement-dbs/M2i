# La classe Voiture
class Voiture():
    # Attribut de classe (cet attribut est accesible directement par la classe, pas besoin d'instancier d'objet)
    nb_voiture = 0
    def_voiture = "Une voiture possede des pneux en général ^^"

    # Le constructeur (avec 4 parametre)
    # self fait référence à l'objet instancié
    def __init__(self, nb_pneu, puissance, couleur, marque):
        self.nb_pneu = nb_pneu
        self.puissance = puissance
        self.couleur = couleur
        self.marque = marque
        Voiture.nb_voiture += 1 # Ici, nous incrémentons l'attribut de classse à chaque instantiation
    
    # Méthode
    def presentation(self):
        print(f"Marque : {self.marque}, Couleur: {self.couleur}")

    # Pour créer une méthode de classe, il nous faut utiliser le décorateur @classmethod
    #
    # Elles ne peuvent, contrairement aux méthodes classique, pas accéder aux attributs d'instance.
    # Elles peuvent cependant accéder aux attributs de classe, par l'utilisation du mot-clé 'cls'
    @classmethod
    def demarrer(cls, texte):
        print(f"Les voiture démarre en faisant : {texte} - {cls.nb_voiture}")


    # Pour créer une méthode static, il nous faut utiliser le decorateur @staticmethod
    #
    # Les méthodes static ne peuvent pas accéder aux attribut d'instance.
    # Elle peuvent cependant accéder aux attributs de classe mais via l'utilisation de la syntaxe Classe.nom_attribut_classe
    # Elles ont pour but principal de permettre le regroupement de fonctionnalité utilitaire.
    @staticmethod
    def presentation(texte):
        print(texte)
        print(Voiture.def_voiture)

class Calculatrice():
    @staticmethod
    def addition(a, b):
        return a + b
    @staticmethod
    def soustraction(a, b):
        return a - b
    
voiture = Voiture(4, 120, "rouge", "ferrari")
voiture2 = Voiture(4, 10, "grise", "coccinel")

# Pour accéder à l'attribut de classe, il nous faut utiliser la syntaxe NomClasse.nom_attribut
print(Voiture.nb_voiture)

# Pour appeler une méthode de classe, on utilise NomClasse.nom_method()
Voiture.demarrer("Vroom")

# Pour appeler une méthode static, on utilise également NomClasse.nom_method()
Voiture.presentation("Les voitures sont vraiment pratique.")
print(Calculatrice.addition(5,7))