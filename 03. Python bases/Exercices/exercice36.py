# Exercice :
# Avec des variables de type dictionnaire dans une liste, vous réaliserez un logiciel pour stocker une série d'adresses avec :
# - numéro de voie
# - complément
# - intitulé de voie
# - commune
# - code postal
#
# Pour ce faire, vous utiliserez des clés de type string qui représenteront les différentes lignes de l'adresse dans le dictionnaire.
#
# Le logiciel devra permettre les opérations suivantes :
# 1. Ajouter une nouvelle adresse à la liste.
# 2. Éditer une adresse existante en modifiant ses informations.
# 3. Supprimer une adresse de la liste.
# 4. Visualiser l'ensemble des adresses stockées.
#
# Chaque adresse sera un dictionnaire contenant les informations suivantes :
# - 'numero' : le numéro de voie.
# - 'complement' : le complément d'adresse (facultatif).
# - 'intitule' : l'intitulé de la voie.
# - 'commune' : le nom de la commune.
# - 'code_postal' : le code postal.
#
# Le programme doit permettre à l'utilisateur de choisir quelle action réaliser, et effectuer cette action sur les adresses stockées.

def input_adress():
    address = {}
    address["N° de voie"] = input("Saisir N° de voie : ")
    address["Complément"] = input("Saisir Complément  : ")
    address["Intitulé"] = input("Saisir Intitulé : ")
    address["Commune"] = input("Saisir Commune : ")
    address["Code postal"] = input("Saisir Code postal: ")
    return address

def display_address(liste_adresses : list):
    print("=== Liste des Adresses ===")
    for adresse in liste_adresses:
        print(f"Adresse N° {liste_adresses.index(adresse)+1}")
        for key,value in adresse.items():
            print(f"  {key} : {value}")

def affiche_menu():
    print("=== Menu ===")
    print("1. Voir les adresses")
    print("2. Ajouter une adresse")
    print("3. Editer une adresse")
    print("4. Supprimmer une adresses")
    print("0. Quitter")

def handle_choice(liste_adresses : list):
    while True:
        affiche_menu()
        choice = input("Votre choix : ")
        while choice not in '12340':
            print("Erreur de choix.. \n")
            choice = input("Votre choix : ")
        match choice:
            case "1":
                if liste_adresses == []:
                    print("Pas encore d'adresse dans la liste !!!")
                else:
                    display_address(liste_adresses)
            case "2":
                liste_adresses.append(input_adress())
            case "3":
                display_address(liste_adresses)
                index = int(input("Numéro de l'adresse a modifier : ")) -1
                liste_adresses[index] = input_adress()
            case "4":
                display_address(liste_adresses)
                index = int(input("Numéro de l'adresse a suppr : ")) -1
                liste_adresses.pop(index)
            case "0":
                print("Aurevoir")
                break

# Programme Principal
list_adress = []
handle_choice(list_adress)