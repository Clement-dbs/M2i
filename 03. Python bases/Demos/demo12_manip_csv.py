import csv

# --- Lecture du fichier CSV ---
fichier = open("noms.csv", "rt", encoding="utf-8")  # lecture texte UTF-8
lecteurCSV = csv.reader(fichier, delimiter=";")     # séparateur : point-virgule
for ligne in lecteurCSV:
    print(ligne)  # Exemple : ['Nom', 'Prénom', 'Age']
fichier.close()

# --- Écriture dans un autre fichier CSV ---
fichier = open("annuaire.csv", "wt", newline="", encoding="utf-8")  # écriture UTF-8
ecrivainCSV = csv.writer(fichier, delimiter="|")                    # séparateur : barre verticale
ecrivainCSV.writerow(["Nom", "Prénom", "Téléphone"])                # ligne d'en-tête
ecrivainCSV.writerow(["Martin", "Julie", "0399731590"])             # ligne de données
fichier.close()
