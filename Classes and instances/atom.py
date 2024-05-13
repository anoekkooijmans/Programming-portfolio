class Atom:
    """
    Represents an atom in the periodic table.

    Attributes:
        symbol (str): The symbol of the atom.
        atomic_number (int): The atomic number of the atom.
        neutron_number (int): The number of neutrons in the nucleus.
        
    Methods:
        proton_number(): Returns the number of protons in the nucleus.
        mass_number(): Returns the sum of protons and neutrons in the nucleus.
    """

    def __init__(self, symbol, atomic_number, neutrons):
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.neutrons = neutrons
    
    def proton_number(self):
        return self.atomic_number
        
    def mass_number(self):
        return self.atomic_number + self.neutrons
    
    def isotope(self, updated_num_neutrons):
        self.neutrons = updated_num_neutrons
        
    def __eq__(self,other):
        if isinstance(other, Atom) and self.symbol == other.symbol:
            return self.mass_number() == other.mass_number()
        return False
        
    def __lt__(self,other):
        if isinstance(other, Atom) and self.symbol == other.symbol:
            return self.mass_number() < other.mass_number()
        raise TypeError("Cannot compare atoms of different elements")
    
    def __le__(self, other):
        if isinstance(other, Atom) and self.symbol == other.symbol:
            return self.mass_number() <= other.mass_number()
        raise TypeError("Cannot compare atoms of different elements")
        
    def __gt__(self, other):
        if isinstance(other, Atom) and self.symbol == other.symbol:
            return self.mass_number() > other.mass_number()
        raise TypeError("Cannot compare atoms of different elements")
        
    def __ge__(self, other):
        if isinstance(other, Atom) and self.symbol == other.symbol:
            return self.mass_number() >= other.mass_number()
        raise TypeError("Cannot compare atoms of different elements")