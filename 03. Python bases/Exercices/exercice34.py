# Exercice :
# Dans cette édition de la course de modules de Tatooine, la position des concurrents est stockée dans une liste.
# Chaque module (ou concurrent) est représenté par son nom dans cette liste.
# Les événements marquants de la course incluent les changements de position des modules suite à divers événements.
#
# Les événements sont les suivants :
# 1. Une panne moteur fait passer le premier module (premier élément de la liste) à la dernière position.
#    Exemple : ['Module A', 'Module B', 'Module C'] -> ['Module B', 'Module C', 'Module A']
#
# 2. Le deuxième module (deuxième élément de la liste) accélère et prend la tête de la course.
#    Exemple : ['Module A', 'Module B', 'Module C'] -> ['Module B', 'Module A', 'Module C']
#
# 3. Le dernier module (dernier élément de la liste) dépasse l'avant-dernier module pour prendre sa place.
#    Exemple : ['Module A', 'Module B', 'Module C'] -> ['Module A', 'Module C', 'Module B']
#
# 4. Un tir de blaster élimine le module en tête de la course (le premier élément de la liste).
#    Exemple : ['Module A', 'Module B', 'Module C'] -> ['Module B', 'Module C']
#
# 5. Un module qu'on pensait éliminé fait son grand retour et rejoint la dernière position de la course.
#    Exemple : ['Module B', 'Module C'] -> ['Module B', 'Module C', 'Module A']
#
# Créer les fonctions suivantes :
#
# 1. panne_moteur : modifie la liste de manière à ce que le premier module passe dernier, le deuxième passe premier,
#    et ainsi de suite. La fonction prendra en entrée une liste de modules et la modifiera.
#
# 2. passe_en_tete : modifie la liste de manière à ce que le premier module passe deuxième et le deuxième module passe premier.
#    La fonction prendra également une liste et changera les positions des deux premiers éléments.
#
# 3. sauve_honneur : modifie la liste pour que le dernier module prenne la place de l'avant-dernier et l'avant-dernier passe dernier.
#    Par exemple, si la liste est ['Module A', 'Module B', 'Module C'], elle deviendra ['Module A', 'Module C', 'Module B'].
#
# 4. tir_blaster : enlève le premier module de la liste (le module en tête de la course).
#    Par exemple, si la liste est ['Module A', 'Module B', 'Module C'], elle deviendra ['Module B', 'Module C'].
#
# 5. retour_inattendu : ajoute un module (qui pourrait être un module "éliminé") à la fin de la liste.
#    Exemple : si la liste est ['Module B', 'Module C'], elle deviendra ['Module B', 'Module C', 'Module A'].

participants = ["Mario", "Luigi", "Link", "Peach", "Kirby"]

def panne_moteur(participants: list) -> list:
    """
    Simule une panne moteur : 
    Le premier participant passe en dernière position.
    """
    if participants:  # Vérifie que la liste n'est pas vide
        premier = participants.pop(0)  # Retire le premier participant
        participants.append(premier)   # Le place en fin de liste
    return participants

def passe_en_tete(participants: list) -> list:
    """
    Le deuxième participant prend la tête de la course.
    """
    if len(participants) > 1:  # Vérifie qu'il y a au moins 2 participants
        participants[0], participants[1] = participants[1], participants[0]  # Échange des places
    return participants

def sauve_honneur(participants: list) -> list:
    """
    Le dernier participant dépasse l'avant-dernier.
    """
    if len(participants) > 1:  # Vérifie qu'il y a au moins 2 participants
        participants[-1], participants[-2] = participants[-2], participants[-1]  # Échange des 2 derniers
    return participants


def tir_blaster(participants: list) -> str:
    """
    Élimine le premier participant de la course.
    Retourne le nom du participant éliminé.
    """
    if participants:
        return participants.pop(0)  # Retire et retourne le premier participant
    return "Aucun participant"

def retour_inattendu(participants: list, participant_touche: str) -> list:
    """
    Un participant éliminé revient en fin de course.
    """
    participants.append(participant_touche)  # Réintègre le participant à la fin
    return participants

def affichage_course(participants: list):
    """
    Affiche la position de chaque participant sous forme de classement.
    """
    affichage = ""
    for position, participant in enumerate(participants, start=1):
        if position == 1:
            affichage += f"1er - {participant}, "
        else:
            affichage += f"{position}ème - {participant}, "
    print(affichage.rstrip(", "))  # Supprime la virgule finale pour un affichage propre

def podium(participants: list):
    """
    Affiche le podium avec les 3 premiers participants.
    """
    if len(participants) < 3:
        print("Pas assez de participants pour un podium.")
    else:
        print(f"""
        🏆 1er : {participants[0]} 🏆

🥈 2ème : {participants[1]}     🥉 3ème : {participants[2]}
        """)

    #  Simulation de la course avec les événements :
print("\n Départ de la course ")
affichage_course(participants)

print("\n Panne moteur ")
affichage_course(panne_moteur(participants))

print("\n Le deuxième prend la tête ")
affichage_course(passe_en_tete(participants))

print("\n Le dernier dépasse l'avant-dernier ")
affichage_course(sauve_honneur(participants))

print("\n Tir de blaster ! ")
participant_blasterise = tir_blaster(participants)
affichage_course(participants)
print(f" {participant_blasterise} a été éliminé !")

print("\n Retour inattendu ! ")
affichage_course(retour_inattendu(participants, participant_blasterise))

print("\n Résultat final ")
podium(participants)