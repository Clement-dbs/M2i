import math

class CompteBancaire(): 
    def __init__(self, numero_compte: int, nom: str, solde: float):
        self.numero_compte = numero_compte
        self.nom = nom
        self.solde = solde

    def versement(self, compte_a_crediter: CompteBancaire, solde_a_crediter: float):
        self.solde -= solde_a_crediter # identique à "self.solde = self.solde - solde_a_crediter"
        compte_a_crediter.solde += solde_a_crediter
    
    def retrait(self, montant: float):
        self.solde -= montant
        if self.solde < 0 :
            self.agios()

    def agios(self):
        self.solde -= math.fabs(self.solde) * 0.05

    def afficher(self): 
        print(f"N°{self.numero_compte}, Nom: {self.nom}, Solde: {self.solde}")

compte1 = CompteBancaire("123", "MR A", 500)
compte2 = CompteBancaire("456", "MR B", 200)

compte1.afficher()
compte2.afficher()

compte1.versement(compte2, 400)
compte1.retrait(200)

compte1.afficher()
compte2.afficher()