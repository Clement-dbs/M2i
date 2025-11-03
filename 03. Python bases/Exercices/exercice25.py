# Exercice :
# Écrivez un algorithme qui affiche les nombres de 1 à 100. Mais pour
# les multiples de 3, affichez "Fizz" à la place du nombre, pour les
# multiples de 5, affichez "Buzz". Pour les nombres qui sont à la fois
# des multiples de 3 et de 5, affichez "FizzBuzz".
#
# Exemple de sortie attendue (de 1 à 6) :
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# ...


# Correction 1
print("Solution 1 :")
print() # saut de ligne 

# Boucle de 1 à 100
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i)