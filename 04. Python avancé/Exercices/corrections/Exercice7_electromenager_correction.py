class Mixeur():
    def allumer(self):
        print("Le mixeur s'allume !")

    def mixer(self):
        print("Le mixeur mixe !")

    def broyer(self):
        print("Le mixeur broye !")

class Broyeur():
    def allumer(self):
        print("Le broyeur s'allume !")

    def broyer(self):
        print("Le broyeur broye !")

class Cookeo(Mixeur):
    def allumer(self):
        print("Le cookeo s'allume !")

    def mixer(self):
        print("Le cookeo mixe !")

    def broyer(self):
        print("Le cookeo broye !")

    def cuire(self):
        print("Le cookeo cuit !")

    def rechauffer(self):
        print("Le cookeo rechauffe !")

class Four():
    def __init__(self, name):
        self.name = name

    def allumer(self):
        print("Le four s'allume !")

    def cuire(self):
        print("Le four cuit !")

    def rechauffer(self):
        print("Le four rechauffe !")

four = Four("THE mega four")
list_electro = [Mixeur(), Broyeur(), Cookeo(), four]

for electro in list_electro:
    electro.allumer()

    if "cuire" in dir(electro.__class__): 
        electro.cuire()

    if "mixer" in dir(electro.__class__): 
        electro.mixer()
