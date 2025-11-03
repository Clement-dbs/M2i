# Pour créer une classe, il nous faut utiliser le mot-clé class suivit du nom
# Par convention, les noms de classe commencent par des majuscules
class Chien():
    # Pour créer un objet à partir de notre classe, il faudra passer
    # par son constructeur définit par __init__(self):
    # En passant des paramètres à cette méthode, on peut les placer dans notre objet
    def __init__(self, nom, age, race):
        self.nom = nom
        self.age = age
        self.race = race

    # Pour créer une méthode, nous devons suivre la même syntaxe qu'une fonction
    # hormis que celle-ci possède un premier parametre self (obligatoire)
    def aboyer(self, texte):
        print(f"{self.nom} aboie sur {texte}")

# Pour créer une instance de notre classe Chien, il nous faut faire appel au constructeur (nom_class(params))
chien = Chien("Idefix", 3, "White terrier")

# Pour accéder aux attributs de l'objet,
# on se sert de la notation nom_instance.nom_attribut
print(chien.nom, chien.age, chien.race)
chien.nom = "Rex"
print(chien.nom)

# Pour appeler une méthode, nous utilisons la syntaxe nom_instance.nom_methode(params)
chien.aboyer("le facteur !")

# Nous pouvons créer autant de chien que nous souhaitons à partir de notre classe.
chien_2 = Chien("Pluto", 4, "Labrador")
print(f"Nom du 2e chien {chien_2.nom}")
chien_2.aboyer("son maître !!")