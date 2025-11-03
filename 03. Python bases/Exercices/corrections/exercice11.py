# Exercice 11

nombre = 10
nombre = int(input("Saisir un nombre : "))

# solution 1
if nombre % 2 == 0:
    print(f"Le nombre {nombre} saisi est pair")
else:
    print(f"Le nombre {nombre} saisi est impair")

# solution 2
print(f"Le nombre {nombre} saisi est pair" if nombre % 2 == 0 else f"Le nombre {nombre} saisi est impair")

