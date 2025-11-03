from enum import Enum, auto

class Couleur(Enum):
    ROUGE = 1
    VERT = 2
    BLEU = 3

print(Couleur.ROUGE)
print(Couleur.ROUGE.name)
print(Couleur.ROUGE.value)

for c in Couleur:
    print(c)

if 1 in Couleur:
    print("Nous avons la couleur rouge")

class Jours(Enum):
    LUNDI = "Lundi"
    MARDI = "Mardi"
    MERCREDI = "Mercredi"

print(Jours.MARDI.value)
print(list(Jours))

if "Mardi" in Jours:
    print("Mardi est présent !")

class Statut(Enum):
    EN_ATTENTE = auto()
    EN_COURS = auto()
    TERMINE = auto()

print(list(Statut))