# Exercice :
# Via l'utilisation d'une variable de type liste, vous devrez réaliser un logiciel permettant à l'utilisateur
# d'entrer une série de notes, dont le nombre possible à entrer sera soit (au choix de l'utilisateur) :
# - saisie avant la saisie de notes
# - permissif et pourra aller jusqu'à entrer une note négative qui stoppera la saisie des notes.
#
# Une fois la saisie des notes terminée, l'utilisateur aura à sa disposition un affichage lui permettant 
# d'avoir la note max, la note min ainsi que la moyenne (possible de faire un menu pour choisir).
#
# Exemple de saisie et d'affichage attendu :
# Veuillez entrer une note entre 0 et 20 compris (une note négative stoppera la saisie) : 12
# Veuillez entrer une note entre 0 et 20 compris (une note négative stoppera la saisie) : 11
# Veuillez entrer une note entre 0 et 20 compris (une note négative stoppera la saisie) : 9
# Veuillez entrer une note entre 0 et 20 compris (une note négative stoppera la saisie) : 8
# Veuillez entrer une note entre 0 et 20 compris (une note négative stoppera la saisie) : 7
# La note maximale est de 12.00 / 20
# La note minimale est de 7.00 / 20
# La moyenne est de 9.40 / 20

def saisie_note_0_20():
    note = float(input("Saisir une note : "))
    while note <0 or note >20:
        note = float(input("Erreur! Saisir une note : "))
    return note

def saisie_note(max,min = 0):
    note = float(input("Saisir une note : "))
    while note <min or note >max:
        note = float(input("Erreur! Saisir une note : "))
    return note

def saisie_nombre_notes():
    nombre = int(input("Combien de notes voulez-vous ? "))
    liste_notes = []
    for i in range(0, nombre):
        liste_notes.append(saisie_note_0_20())
    return liste_notes

def saisie_nombre_notes_avec_message(message: str) -> list:
    nombre = int(input(message))
    liste_notes = []
    for i in range(0, nombre):
        liste_notes.append(saisie_note_0_20())
    return liste_notes

def saisie_notes_negatif_stop():
    liste_notes = []
    while True:
        note = float(input("Saisir une note : "))
        if note <0 or note >20:
            print("Note erronée, on arrête la saisie")
            break
        else:
            liste_notes.append(note)
    return liste_notes
        
def saisie_notes_menu():
    while True:
        print("[1] Pour entrer un nombre de note connu\n[2] Pour continuer la saisie jusqu'a une note negative")
        choix = input("Votre choix : ")
        match choix:
            case "1":
                return saisie_nombre_notes()
            case "2":
                return saisie_notes_negatif_stop()
            case _:
                print("Votre choix ne correspond pas")

def menu_min_max_moy(liste_notes):
    while True:
        print("Faites votre choix :")
        print("1 - Afficher note minimale")
        print("2 - Afficher note maximale")
        print("3 - Afficher moyenne")
        print("4 - Quitter programme")
        choix_Menu = input("Votre choix : ")
        match choix_Menu:
            case "1":
                print(min(liste_notes))
            case "2":
                print(max(liste_notes))
            case "3":
                print(sum(liste_notes)/len(liste_notes))
            case "4":
                exit()
            case _:
                print("Erreur, réessayez !\n")


def main():
    liste_notes = saisie_notes_menu()
    menu_min_max_moy(liste_notes)
    

if __name__ == "__main__":
    main()
