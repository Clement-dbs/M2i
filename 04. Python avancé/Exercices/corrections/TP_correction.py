from abc import ABC, abstractmethod
from enum import Enum, auto

class Document(ABC):
    nb_document = 0

    def __init__(self, titre: str, annee_publication: int):
        self.titre = titre 
        self.annee_publication = annee_publication

    @abstractmethod
    def afficher_infos(self):
        pass

    @classmethod
    def afficher_nb_document(cls):
        print(f"Nous avonc actuellement {cls.nb_document} documents dans notre bibliotheque.")

class Genre(Enum):
    ROMAN = auto()
    SCIENCE_FICTION = auto()
    FANTASTIQUE = auto()

class Empruntable(ABC):
    def __init__(self):
        self.est_emprunte = False

    @abstractmethod
    def emprunter(self):
        pass

    @abstractmethod
    def rendre(self):
        pass

class Consultable(ABC):
    @abstractmethod
    def consulter(self):
        print("Vous consultez ce document.")

class DocumentDejaEmprunteException(Exception):
    pass

class DocumentNonEmprunteException(Exception):
    pass


class Livre(Document, Empruntable, Consultable):
    def __init__(self, titre: str, annee_publication: int, auteur: str, nb_pages: int, genre: Genre):
        super().__init__(titre, annee_publication)
        Empruntable.__init__(self)
        self.auteur = auteur
        self.nb_pages = nb_pages
        self.genre = genre

    @staticmethod
    def constructeur_secondaire(self, titre: str, auteur: str, genre: Genre):
        return Livre(titre, 0, auteur, 100, genre)
    
    @staticmethod
    def compterPages(liste_livre: list):
        total = 0
        for livre in liste_livre:
            total += livre.nb_pages
        
        return total
    
    def afficher_infos(self):
        print(f"Livre ({self.titre, self.auteur, self.annee_publication, self.nb_pages, self.genre.name})")

    def emprunter(self):
        if self.est_emprunte == True: 
            raise DocumentDejaEmprunteException("Vous ne pouvez pas emprunter un livre déjà emprunté...")
        else:
            print("Emprunt réussi !")
            self.est_emprunte = True

    def rendre(self):
        if self.est_emprunte == False: 
            raise DocumentNonEmprunteException("Vous ne pouvez pas rendre un livre qui n'a pas été emprunté...")
        else:
            print("Le livre est maintenant disponible.")
            self.est_emprunte = False
        
    def consulter(self):
        super().consulter()
    
class Magazine(Document, Consultable):
    def __init__(self, titre, annee_publication, numero):
        super().__init__(titre, annee_publication)
        self.numero = numero

    def afficher_infos(self):
        print(f"Magazine ({self.titre, self.annee_publication, self.numero})")

    def consulter(self):
        super().consulter()

def menu():
    return """
    ====== GESTION BIBLIOTHEQUE ======
    1. Consulter
    2. Emprunt
    3. Restitution
    0. Quitter
    """

def display_liste(liste_livre):
    cpt = 1
    for livre in list_livre:
        print(cpt,". ", end="")
        livre.afficher_infos()
        cpt += 1

def choisir_document(liste_livre) -> int: 
    display_liste(liste_livre)
    user_livre_choice = int(input("Veuillez choisir le livre : "))

    return user_livre_choice

list_livre = [
    Livre("The witcher", 2000, "Andrej", 600, Genre.FANTASTIQUE),
    Livre("les 12 travaux", 1990, "Socrate", 500, Genre.ROMAN),
    Magazine("Canard PC", 2000, 3),
    ]


while True:
    print(menu())
    user_choice = int(input("Veuillez faire un choix : "))

    match user_choice:
        case 1 :
            livre_id = choisir_document(list_livre)
            list_livre[livre_id-1].consulter()
        case 2 :
            livre_id = choisir_document(list_livre)
            try:
                list_livre[livre_id-1].emprunter()
            except DocumentDejaEmprunteException as e:
                print(e)
        case 3: 
            livre_id = choisir_document(list_livre)
            try:
                list_livre[livre_id-1].rendre()
            except DocumentNonEmprunteException as e:
                print(e)
        case 0:
            break
        case _:
            print("Erreur, choix indisponible")