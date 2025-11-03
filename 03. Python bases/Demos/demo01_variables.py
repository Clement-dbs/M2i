# Les commentaires
# Si j'ecrit sur plusieurs
# lignes je peut les commenter 

# Print
print("Hello World !!!")
# pour lancer mon script j'ouvre un terminal :
# python demo01_varaibles.py 

# print sur plusieurs lignes
# print("""Hello
      
#       World
      
#       !!!""")

# print multiple avec des espaces
print(1,"test",1.9,"coucou")

# Variables
ma_variable = 8
print(ma_variable)

# varaible numerique
var = 23 #int
print(var)
print(type(var))
var = 23.12 #float
print(var)
print(type(var))

# le type chaine
var = "23.0" #str
print(var)
print(type(var))

# les booleens
mon_bool = True
print(mon_bool)
mon_bool = False
print(mon_bool)
print(type(mon_bool))

# Les comparaisons renvoie un type booleens
print(4 < 5) # True
print(5 > 4) # True
print(5 >= 5) # True
print(5 <= 5) # True
print(5 == 5) # True
print(5 != 5) # False

# input 
print("saisir un entier :")
ma_variable = input()
print("Vous avez saisie : ",ma_variable)
print("Type de ce que vous avez saisie : ",type(ma_variable))

# Le cast (passer d'un type de variable a l'autre)
var_int = int(ma_variable)
print(var_int)
print(type(var_int))
var_float = float(ma_variable)
print(var_float)
print(type(var_float))

# input sur une ligne
variable = input("Saisir quelque chose : ")
print(variable)