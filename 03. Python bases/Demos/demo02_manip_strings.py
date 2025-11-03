# Concatenantion
str1 = "chaine 1"
str2 = "chaine 2"
str3 = "chaine 3"
print(str1)
print(str2)
print(str3)
print(str1 + str2)

# equivalent
print(str1 + " " + str2)
print(str1,str2)
str4 = "str1 : "+str1+" str2 : "+str2
print(str4)

# Concatenation avec des entier
mon_entier = 25
ma_chaine= "J'ai "
ma_chaine2= " ans"
print(ma_chaine + str(mon_entier) + ma_chaine2)
print(ma_chaine,mon_entier,ma_chaine2)

# Chaine formatees
#.format
prenom = "Toto"
ma_chaine_formatee = "J'ai {0} ans et je m'apelle {1} (age = {0})".format(mon_entier,prenom)
print(ma_chaine_formatee)
ma_chaine_formatee2 = f"J'ai {mon_entier} ans et je m'apelle {prenom} age = {mon_entier}"
print(ma_chaine_formatee2)

# caracteres speciaux
# retour a la ligne \n
chaine = "Ligne 1\nLigne 2\nLigne 3"
print(chaine)
# tabulation
chaine = "Ligne 1 \n\tLigne 2\n\t\tLigne 3"
print(chaine)

# les guillemets
chaine ="l'alouette"
print(chaine)
chaine = 'l\'alouette'
print(chaine)

# Decoupage de chaines
chaine = "abcdefghi"

# Recuperer un seul caractere avec son indice
print(chaine)
print(chaine[4])
print(chaine[0])
# print(chaine[99])
print(chaine[0] + chaine[8])

# Decouper une chaine avec un debut et une fin
print(chaine[0:4])
print(chaine[:4])
print(chaine[2:4] + chaine[6:])

# si pas de debut ou fin on prend tout
print(chaine[:])

# decouper notre chaine un pas
# chaine[debut:fin:pas]
chaine = "abcdefghi"
print(chaine[::2])

print(chaine[-2])
print(chaine[-3:])