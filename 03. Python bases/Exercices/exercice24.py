# Exercice :
# Soit un capital `c` placé à un taux `t`. On veut connaître le nombre
# d'années nécessaire au doublement de ce capital.
# Exemple de calcul (le taux est de 4%, soit 0,04) :
# Cn = 10 000 x (1+0,04)^5 = 12 166 euros, soit un gain de 2 166 euros.


# c = float(input("Sasir le capital initial "))
t = float(input("Entre le taux (en pourcentage) : ")) /100

# capital = c
# annees = 0

# while capital < 2*c:
#     capital *= (1 + t)
#     annees += 1

# print(f"Le capital double en {annees}")

c = 1
annees = 0

while c < 2:
    c *= (1 + t)
    annees += 1

print(f"Le capital double en {annees}")