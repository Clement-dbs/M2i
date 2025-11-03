# la boucle for

# for i in range(5): # de 0 à 4 (5 exclus)
#     print(f"Itération n°:{i}")

# for i in range(2,5): # de 2 à 4 (5 exclus)
#     print(f"Itération n°:{i}")

# for i in range(2,10,2): # de 2 à 9 (10 exclus) avec un pas de 2
#     print(f"Itération n°:{i}")

# la boucle while

# compteur = 0
# while compteur < 5:
#     compteur +=1 
#     print(f"Compteur : {compteur}")
#     #compteur +=1 

# for i in range(10):
#     if i == 5:
#         break
#     print(f"i = {i}")

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(f"Nombre impair = {i}")

# utilisation d'une boucle avec else
# for i in range(3):
#     print(f"Essai {i}")
# else:
#     print("La booucle se termine normalement")

# for i in range(3):
#     print(f"Essai {i}")
#     if i == 1:
#         break
# else:
#     print("ce message ne s'affichera pas")

# boucles imbriquees
# for i in range(3):
#     for j in range(2):
#         print(f"i = {i}, j = {j}")

# boucle avec liste
elements = ["Voiture","Velo","Metro"]
for transport in elements:
    print(f"Element : {transport}")

mot = "Bonjour salut"
for caractere in mot:
    print(f"Lettre : {caractere}")

