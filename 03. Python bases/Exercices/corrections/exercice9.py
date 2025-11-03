# Exercice 9
import math

rayon = float(input("Saisir un rayon : "))
hauteur = float(input("Saisir une hauteur : "))

volume = (1/3) * math.pi * (rayon*rayon) * hauteur

print(f"Le volume du cône est d'environ : {round(volume)}cm3")