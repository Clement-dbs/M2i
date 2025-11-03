nombre1 = input("Saisir le nombre 1 :")
nombre2 = input("Saisir le nombre 2 :")
nombre3 = input("Saisir le nombre 3 :")

if nombre1 >= nombre2 and nombre1 >= nombre3:
    maximum = nombre1
elif nombre2 >= nombre1 and nombre2 >= nombre3:
    maximum = nombre2
else:
    maximum = nombre3

print(f"La valeur maximale est : {maximum}")
# solution 2
print(f"La valeur maximale est : {max(nombre1,nombre2,nombre3)}")