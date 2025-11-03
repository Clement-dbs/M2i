class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)

    def show(self):
        print(self.street)
        print(self.city)

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email= email

    def show(self):
        print(self.name + ' - ' + self.email)

class Contact(Address, Person):
    def __init__(self, name, email, street, city):
        Address.__init__(self, street, city) 
        Person.__init__(self, name, email)

    def show(self):
        Person.show(self)
        Address.show(self)

class Notebook():
    def __init__(self, dictionnary: dict = {}):
        self.dictionnary = dictionnary

    def add(self, name, email, street, city): 
        self.dictionnary[name] = Contact(name, email, street, city)

    def show(self):
        for contact in self.dictionnary.values():
            contact.show()

notebook = Notebook({"Tata": Contact("Tata", "tata@test.test", "rue", "ville")})
notebook.show()

notebook.add("Titi","titi@test.test", "rue", "ville")
notebook.show()