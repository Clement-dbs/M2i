# Exercice :
# Écrire un algorithme qui demande successivement 6 nombres à l'utilisateur,
# et qui lui dit ensuite quel était le plus grand parmi ces 6 nombres.

# solution 1
# max_nombre = float(input("Entrez un nombre :")) 

# for _ in range(5):
#     nombre = float(input("Entrez un nombre :"))
#     if nombre > max_nombre:
#         max_nombre = nombre

# print(f"Le plus grand nombre saisi est {max_nombre}")

# solution 2
# max_nombre = float(input("Entrez un nombre :")) 

# compteur = 1
# while compteur < 6:
#     nombre = float(input("Entrez un nombre :"))
#     if nombre > max_nombre:
#         max_nombre = nombre
#     compteur += 1

# print(f"Le plus grand nombre saisi est {max_nombre}")

# solution 3

max_nombre = max(float(input("saisir un nombre :")) for _ in range(6))
print(f"Le plus grand nombre saisi est {max_nombre}")