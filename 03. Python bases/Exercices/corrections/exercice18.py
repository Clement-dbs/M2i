# Exercice 18

temperature = float(input("Saisir une température :"))

if temperature < 0:
    print("SOLIDE")
elif temperature > 100:
    print("GAZEUX")
else:
    print("LIQUIDE")

if temperature < 0:
    print("SOLIDE")
#elif temperature >=0 and temperature <= 100:
elif temperature <= 100:
    print("LIQUIDE")
else:
    print("GAZEUX")

#if temperature >= 0 and temperature <= 100:
if 0 <= temperature <= 100:
    print("LIQUIDE")
elif temperature > 100:
    print("GAZEUX")
else:
    print("SOLIDE")