# Exercice :
# Réaliser un programme permettant à l'utilisateur d'entrer comme données :
# - Une population initiale.
# - Un taux d'accroissement.
# - Une population visée.
# Ce programme permettra à l'utilisateur de savoir en combien de temps la population visée sera atteinte.

population_initiale = int(input("Entrez la population initiale :"))
taux_accroissement = float(input("Entrez le taux d'acreoissement annuel (en pourcentage) :")) /100
population_visee = int(input("Entrez la population visée :"))

# Initialisation
population = population_initiale
annees = 0

# boucle jusqu'a atteindre ou depasser la population visee
while population < population_visee:
    #population = population * (1+taux_accroissement)
    population *= (1+taux_accroissement)
    annees += 1
    print(f"{annees} ans et passe la population est de {population}")

print(f"La population atteindra {population_visee} en {annees} ans.")
