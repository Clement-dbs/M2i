class Chien():

    def __init__(self, nom, age, race):
        self.nom = nom # attribut public
        self._age = age # attribut protected
        self.__race = race # attribut private

    # Le decorateur @property permet de définir le getter pour accéder à l'attribut age (lecture seule)
    @property
    def age(self):
        return self._age 
    
    # Le decorateur @nom_property.setter permet de modifier l'attribut correspondant (écriture seule)
    # Il n'est pas obligatoire si l'on souhaite que l'attribut soit non-modifiable
    @age.setter
    def age(self, age):
        if age > 0 and age < 20: 
            self._age = age
        else: 
            print(f"Erreur, {age} est un age incorrect..")
    
    # Il est également possible de définir les propriété de manière plus "classique" avec des méthodes getter/setter 
    def get_race(self):
        return str.upper(self.__race)
    
    def set_race(self, race: str):
        self.__race = race
    
    
chien = Chien("Rex", 5, "Berger Allemand")
print(chien.nom) # Attribut public donc accès direct à celui-ci
print(chien.age) # Attribut avec @property donc accès via celui-ci
chien.age = 10 # Modifier via @age.setter
print(chien.age)

chien.age = 50 # Affichage d'une erreur (car age non-compris entre 0 et 10)
print(chien.age)

chien._Chien__race = "Labrador" # Accès direct à la variable "privé"  
print(chien._Chien__race)

chien.set_race("Berger Allemand")
print(chien.get_race())
