class WaterTank():
    all_watertanks_water_level = 0
    all_watertanks_weight = 0

    def __init__(self, weight: float, max_capacity: float, water_level: float = 0):
        self.weight = weight
        self.max_capacity = max_capacity

        if water_level > max_capacity:
            water_level = max_capacity
        self.water_level = water_level

        WaterTank.all_watertanks_water_level += water_level
        WaterTank.all_watertanks_weight += weight

    def total_weight(self):
        return self.weight + self.water_level
    
    def fill(self, amount):
        if amount < 0: 
            amount = 0

        exceed_water = 0
        if amount + self.water_level > self.max_capacity: 
            exceed_water = (amount + self.water_level) - self.max_capacity
            self.water_level = self.max_capacity
            WaterTank.all_watertanks_water_level += amount - exceed_water
        else:
            self.water_level += amount
            WaterTank.all_watertanks_water_level += amount

        return exceed_water
    
    def empty(self, amount):
        if amount < 0: 
            amount = 0

        water_taken = 0
        if amount > self.water_level:
            water_taken = self.water_level
            self.water_level = 0
            WaterTank.all_watertanks_water_level -= water_taken
        else:
            water_taken = amount
            self.water_level -= amount
            WaterTank.all_watertanks_water_level -= amount

        return water_taken
    
    def afficher(self):
        print(f"Citerne (Poids vide : {self.weight}, Cap max: {self.max_capacity}, Niveau: {self.water_level})")

if __name__ == "__main__": 
    watertank1 = WaterTank(10, 20, 10)
    watertank2 = WaterTank(5, 10, 10)

    print(f"Poids total de la citerne 1 : {watertank1.total_weight()}")
    print(f"Poids total de la citerne 2 : {watertank2.total_weight()}")

    print("-"*80)

    print(f"Quantité d'eau de la citerne 1 : {watertank1.water_level}")
    print(f"Quantité d'eau de la citerne 2 : {watertank2.water_level}")
    print(f"Quantité d'eau dans toutes les citernes : {WaterTank.all_watertanks_water_level}")

    print("-"*80)

    excess_water = watertank1.fill(11)
    print(f"Quantité d'eau dans la citerne après ajout de 11L : {watertank1.water_level}")
    print(f"Excès d'eau récupéré: {excess_water}")

    water_taken = watertank2.empty(11)
    print(f"Quantité d'eau dans la citerne après avoir retiré 11L : {watertank2.water_level}")
    print(f"Eau récupéré: {water_taken}")

    print("-"*80)

    print(f"Quantité d'eau de la citerne 1 : {watertank1.water_level}")
    print(f"Quantité d'eau de la citerne 2 : {watertank2.water_level}")
    print(f"Quantité d'eau dans toutes les citernes : {WaterTank.all_watertanks_water_level}")

    print(f"Poids total de toutes les citernes : {WaterTank.all_watertanks_water_level + WaterTank.all_watertanks_weight} KG")