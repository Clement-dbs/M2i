# Exercice :
# Ce programme demande à l'utilisateur de saisir une chaîne d'ADN ainsi qu'une séquence d'ADN,
# puis retourne le nombre d'occurrences de cette séquence dans la chaîne d'ADN.
# 
# **Clarification :** Malgré les termes "chaîne d'ADN" et "séquence d'ADN", il s'agit en réalité
# de rechercher une sous-chaîne (séquence) dans une autre chaîne de caractères.
# Vous devez simplement compter combien de fois une séquence donnée apparaît dans la chaîne.
#
# La chaîne et la séquence seront composées uniquement des lettres suivantes : 'a', 't', 'c', 'g'.
#
# 1. Écrire une fonction `vérification_adn` qui permet de renvoyer la valeur True si la chaîne d'ADN est valide
#    (c'est-à-dire qu'elle contient uniquement les caractères 'a', 't', 'c', 'g'), False si elle est invalide.
#
# 2. Écrire une fonction `saisie_adn` qui récupère la saisie de l'utilisateur, vérifie sa validité
#    et renvoie une chaîne d'ADN valide sous forme de chaîne.
#
# 3. Écrire une fonction `proportion` qui reçoit deux paramètres : une chaîne d'ADN et une séquence d'ADN.
#    Elle renverra le nombre d'occurrences de la séquence dans la chaîne, autrement dit, combien de fois
#    cette sous-chaîne apparaît dans la chaîne principale.
#
# 4. Créer des instructions pour tester le programme, en vérifiant que l'utilisateur peut saisir une chaîne et une séquence
#    et que le programme renvoie le bon nombre d'occurrences de cette séquence dans la chaîne.


def verification_adn(chaine):
    """
    Vérifie si la chaîne contient uniquement des caractères valides : 'a', 'c', 't', 'g'.
    Retourne True si valide, False sinon.
    """
    for lettre in chaine:
        if lettre not in "actg":
            return False
    return True

# print(verification_adn("abecededeg"))
# print(verification_adn("agtctgatgta"))

def saisie_adn(question):
    """
    Demande une saisie utilisateur et vérifie qu'il s'agit d'une chaîne ADN valide.
    Continue de demander une saisie jusqu'à ce que l'entrée soit correcte.
    """
    while True:
        chaine = input(question).lower()  
        if verification_adn(chaine):
            return chaine
        print("Erreur : La chaîne doit contenir uniquement 'a', 't', 'c' ou 'g'. Veuillez réessayer.")


# test_chaine = saisie_adn("Saisir une chaine ADN (atcg):")
# print("chaine ok : ",test_chaine)

def compter_occurrences(sequence, chaine):
    """
    Compte le nombre de fois où la séquence apparaît dans la chaîne ADN.
    """
    return chaine.count(sequence)


def calculer_pourcentage(sequence, chaine, occurrences):
    """
    Calcule le pourcentage de la séquence dans la chaîne ADN.
    Formule : (nombre d'occurrences * longueur de la séquence) / longueur de la chaîne * 100
    """
    if len(chaine) == 0:  # Éviter la division par zéro si la chaîne est vide
        return 0
    return (occurrences * len(sequence) / len(chaine)) * 100



# Programme principal

# Demander a l'utilsateur la chaine ADN
chaine_adn = saisie_adn("Saisir la chaine ADN : ")

# Demander a l'utilsateur la sequence ADN
sequence_adn = saisie_adn("Saisir a present la sequence ADN :")

# Valeur Saisie
print(f"Chaine ADN : {chaine_adn}")
print(f"Sequence ADN : {sequence_adn}")

# Calcul
occurrence = compter_occurrences(sequence_adn,chaine_adn)
pourcentage = calculer_pourcentage(sequence_adn,chaine_adn,occurrence)
print(f"La sequence {sequence_adn} apparait {occurrence} fois dans la chaine {chaine_adn}")
print(f"Elle represente {pourcentage}% de la chaine")