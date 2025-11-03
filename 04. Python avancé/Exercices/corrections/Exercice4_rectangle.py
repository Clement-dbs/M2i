class Rectangle():
    def __init__(self, longueur: int, largeur: int):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        return (self.longueur + self.largeur) * 2
    
    def surface(self):
        return self.largeur * self.longueur
    
rectangle = Rectangle(5, 5)
print(f"Le perimetre du rectangle est de : {rectangle.perimetre()}")
print(f"La surface du rectangle est de : {rectangle.surface()}")

class Pave(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def perimetre(self):
        return (super().perimetre() * 2) + 4*self.hauteur

    def surface(self):
        return (super().surface() * 2) + (self.hauteur * self.longueur) *2 + (self.hauteur * self.largeur) * 2
    
    def volume(self):
        return super().surface() * self.hauteur
    
pave = Pave(5,5,5)
print(f"Le perimetre du pave est de : {pave.perimetre()}")
print(f"La surface du pave est de : {pave.surface()}")
print(f"Le volume du pave est de : {pave.volume()}")