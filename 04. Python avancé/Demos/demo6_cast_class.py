class Ordinateur(): 

    def __init__(self, nom, prix, marque, quantite):
        self.nom = nom
        self.prix = prix
        self.marque = marque
        self.quantite = quantite

    def afficher(self):
        print("Mon ordinateur :")
        print("Nom : ", self.nom)
        print("Prix : ", self.prix)
        print("Marque : ", self.marque)
        print("Quantité : ", self.quantite)

    # Ici, on redéfinit une méthode de cast en string de notre Ordinateur (ordinateur -> str)
    def __str__(self):
        return f"Ordinateur (nom : {self.nom}, prix : {self.prix}, marque : {self.marque}, quantité : {self.quantite})"
    
    # Ici, on rédéfinit une méthode pour récupérer la length de notre objet
    def __len__(self):
        return self.quantite
    
    # Ici, repr permet de donner une représentation technique de notre objet (pour les dev)
    def __repr__(self):
        return f"({self.nom}, {self.prix}, {self.marque}, {self.quantite})"
    
    # Ici, nous récupérons la représentation de notre classe quand elle est cast en float
    def __float__(self):
        return self.prix
    
    # Ici, nous récupérons la représentation de notre classe quand elle est cast en booléen
    def __bool__(self):
        return self.quantite > 0 
    
    # Ici, nous donnons le résultat de l'addition de 2 objets 'Ordinateur'
    def __add__(self, other:Ordinateur):
        return self.prix + other.prix
    
    # Ici, nous donnons l'égalité entre 2 objets
    def __eq__(self, other: Ordinateur):
        # Pour que 2 ordinateurs soient considérés comme identique alors toutes leurs valeurs (sauf quantité)
        # doivent être indentiques.
        return self.nom == other.nom and self.prix == other.prix and self.marque == self.marque

ordinateur = Ordinateur("Best PC ++",499.99,"MSI", 5)

ordinateur.afficher()
print(ordinateur) 
print(len(ordinateur))
print(repr(ordinateur))
print(3 * float(ordinateur))

if bool(ordinateur): 
    print("Il me reste du stock")

ordinateur2 = Ordinateur("Plus Ultra", 1200.00, "AlienWare", 1)

print(f"Addition de 2 ordinateur : {ordinateur + ordinateur2}")

ordinateur3 = Ordinateur("Best PC ++",499.99,"MSI", 10)

if ordinateur == ordinateur3:
    print("Les 2 ordinateurs sont identiques")
