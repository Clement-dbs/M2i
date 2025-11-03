import mon_module
# import module_utilisation
from module_utilisation import version

print(mon_module.saluer("christophe"))
# print(module_utilisation.version)
print(version)

print("Valeur de la variable __name__ dans programme.py : ",__name__)

from random import randint

print("Nombre aleatoire entre 1 et 10 :",randint(1,10))
print(randint.__doc__)

import datetime as dt# importation avec un alias
# from datetime import *
# import datetime
print("Date et heure actuelles : ",dt.datetime.now())
