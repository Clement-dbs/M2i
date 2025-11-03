class Chien():
    def __init__(self, nom, age, race):
        self._nom = nom
        self._age = age
        self._race = race

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    def afficher_chien(self):
        print(f"Nom: {self._nom}, Age: {self.age}, Race: {self._race}")

def menu():
    print("=== MENU PRINCIPAL ===")
    print("1. Voir les chiens")
    print("2. Ajouter un chien")
    print("3. Retirer un chien")
    print("4. Ajouter un an aux chiens")
    print("0. Quitter")

def ajouter_chien():
    nom = input("Veuillez saisir un nom : ")
    age = int(input("Veuillez saisir un age : "))
    race = input("Veuillez saisir la race : ")
    liste_chiens.append(Chien(nom, age, race))

def afficher_chien():
    cpt = 0 
    for chien in liste_chiens:
        cpt += 1
        print(f"{cpt}. ", end="")
        chien.afficher_chien()

liste_chiens = [Chien("Rex", 5, "Berger Allemand"), Chien("Polochon", 4, "Bogtail")]

while True:
    menu()
    user_input = int(input("Veuillez faire un choix : "))

    match user_input: 
        case 1:
            afficher_chien()
        case 2:
            ajouter_chien()
        case 3:
            afficher_chien()
            id = int(input("Veuillez saisir l'id du chien à retirer : "))
            liste_chiens.pop(id-1)
        case 4:
            for chien in liste_chiens:
                chien.age += 1
        case 0:
            break
        case _ :
            print("Erreur, mauvais choix!")
    