# Exercice :
# Écrire un algorithme permettant d'afficher la table de multiplication par 9.

print("Table de multiplaction par 9 :")
for i in range(1,11):
    print(f"9 x {i} = {9*i}")

# solution 2
i = 1
while i <= 10:
    print(f"9 x {i} = {9*i}")
    i += 1