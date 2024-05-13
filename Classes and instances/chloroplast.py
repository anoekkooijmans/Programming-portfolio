class Chloroplast:
    """
    Represents a chloroplast, a cell organelle responsible for photosynthesis.
    
    Attributes:
        water (int): The number of water molecules stored in the chloroplast.
        co2 (int): The number of carbon dioxide molecules stored in the chloroplast.
        
    Methods:
        add_molecule(): Adds a molecule of water or carbon dioxide to the chloroplast.
        photosynthesis(): Initiates the photosynthesis process if enough CO2 and water molecules are present.      
    """
    
    def __init__(self):
        self.water = 0
        self.co2 = 0
    
    def add_molecule(self, molecule):
        if molecule == "water":
            self.water += 1
        elif molecule == "co2":
            self.co2 += 1
        else:
            raise ValueError("Only water and co2 molecules can be added.")
        return []
            
    def photosynthesis(self):
        if self.co2 >= 6 and self.water >=12:
            self.co2 -= 6
            self.water -= 12
            sugar = ("C6H12O6", 1)
            oxygen = ("O2", 6)
            return [sugar, oxygen]
        else:
            return []
    
    def __str__(self):
        return f"Water molecules: {self.water}\nCO2 molecules: {self.co2}"