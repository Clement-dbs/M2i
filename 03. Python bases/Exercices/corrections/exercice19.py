# Exercice 19

age = int(input("saisir un age :"))
salaire = float(input("saisir un salaire souhaite :"))
experience = int(input("saisir le nombre d'annees d'experiences :"))

valide = True

if age <= 30:
    print("Vous etes trop jeune")
    valide = False

if salaire > 40000:
    print("Le salaire demande est trop élevé")
    valide = False

if experience < 5:
    print("Vous manquez d'experience")
    valide = False

if valide:
    print("Votre profil correspond aux postes")
else:
    print("Merci pour votre candidature")