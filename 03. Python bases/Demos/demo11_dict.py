# pour créer un dictionnaire
mon_dict = {} #ne pas confondre avec le set vide (set())

mon_dict = {
    "clé 1": "valeur 1", 
    2: 2, 
    True: False, 
    # ["premier element liste"]: {"valeur1 set"} 
    # une liste avec un set en valeur -> impossible car les clés ne sont que des types simples/primitifs (bool, str, float, int)
}
mon_dict = {
    "test": "valeur pour la clé test",
    1: 340,
    'test': True # la clé étant unique, ici, on remplace la valeur de test
}
print(mon_dict)

# Pour accéder à la valeur liée à la clé d'un dictionnaire,
# on se sert de la syntaxe ci-dessous
print(mon_dict[1])
print(mon_dict['test'])

# Pour ajouter un élément dans un dictionnaire,
# on crée une clé et on lui donne sa valeur
mon_dict['blabla'] = 'Texte lié à blabla'
print(mon_dict)

# Ici , on re-affecte la valeur de 'blabla' à autre chose
mon_dict['blabla'] = 247
print(mon_dict)

# Pour obtenir la liste des clés de notre dictionnaire, il existe la méthode .keys()
print(mon_dict.keys())
for k in mon_dict.keys():
    print(k)
    print(mon_dict[k])

# Pour obtenir les valeurs de notre dictionnaire, il existe la méthode .values()
print(mon_dict.values())
for v in mon_dict.values():
    print(v)

print(mon_dict.items())
print(type(mon_dict.items()))

# les 3 boucles suivantes font la même chose
for tuple in mon_dict.items():
    cle, valeur = tuple
    print(cle, valeur)

for cle, valeur in mon_dict.items():
    print(cle, valeur)

print(mon_dict.keys())
for k in mon_dict.keys():
    print(k, mon_dict[k]) #on accède à la valeur de mon dict pour la clé k

for k in mon_dict: #par défaut on itère sur les clés
    print(k, mon_dict[k])

# Pour supprimer une entrée du dictionnaire on peut utiliser cette méthode
# Attention : Exception si la clé n'existe pas !
del mon_dict['blabla']
print(mon_dict)

# Il existe aussi la méthode .pop() dans laquelle il va falloir renseigner la clé
# Attention : Exception si la clé n'existe pas !
print(mon_dict.pop('test'))
print(mon_dict)

mon_dict = {
    "clé 1": "valeur 1", 
    2: 2, 
    True: False, 
}
# Pour fusionner deux dictionnaires ensemble, il existe la méthode .update()
mon_dict.update({2: "Valeur de clé 2", 'test': 'valeur test'})
# dict2 = {2: "Valeur de clé 2", 'test': 'valeur test'}
# mon_dict.update(dict2)
print(mon_dict)