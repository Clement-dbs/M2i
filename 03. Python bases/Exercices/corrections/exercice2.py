# Exercice 2

a = 1
b = 2
a = b
b = a

print("a = ",a)
print("b = ",b)

# - Les deux dernières instructions permeient-elles d’échanger les valeurs de A et B ? NON

# - Ecrire un algorithme permettant d’échanger les valeurs de deux variables A et B
# solution 1
print("solution 1")
a = 1
b = 2
c = a
a = b
b = c

print("a = ",a)
print("b = ",b)

# solution 2
print("solution 2")
a = 1
b = 2
a,b = b,a

print("a = ",a)
print("b = ",b)