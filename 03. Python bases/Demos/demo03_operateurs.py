import math
from math import pi
# import math as mon_module_math

print(5/3) # division classique
print(5//3) # division entiere (sans virgule dont un int est renvoye)
print(5%3) # modulo
print(2 ** 10) # puissance dix

print(pow(4,2)) # carré de base (pareil que **)
# print(math.pow(4,2)) # carré du module math (pareil que **)
# print(mon_module_math.pow(4,2))  # carré du module math (module renommé)

# module math
var = 0.9999999
print(math.ceil(var))
print(round(var))
print(round(1.4))
print(round(1.5))
print(math.floor(var))

print(math.pi)
print(pi)

# Les comparaisons renvoie un type booleens
print(4 < 5) # True
print(5 > 4) # True
print(5 >= 5) # True
print(5 <= 5) # True
print(5 == 5) # True
print(5 != 5) # False

# Operateurs logiques
print((25 > 5) and (125 != 2)) # ET
print((25 > 5) & (125 != 2)) # ET

print((25 > 50) or (125 != 2)) # OU
print((25 > 50) | (125 != 2)) # OU

print((25 > 50) ^ (125 != 2)) # OU EXCLUSIF

print(not True)