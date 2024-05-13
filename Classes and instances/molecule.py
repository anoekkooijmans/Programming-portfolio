class Molecule:
    """
    Represents a molecule composed of Atom-objects
    
    Attributes:
        atom_quantity(list): A list of tuples, the first element is the Atom-object, 
            the second is the number of atoms of that type that is put into the molecule
            
    Methods:
        molecular_formula(): Returns the molecular formula of the molecule
    """

    def __init__(self, atom_quantity):
        self.atoms = atom_quantity
        
    def __str__(self):
        return self.molecular_formula()
    
    def __add__(self, other):
        new_atoms = self.atoms + other.atoms
        return Molecule(new_atoms)
    
    def molecular_formula(self):
        formula = ""
        for atom, quantity in self.atoms:
            formula += atom.symbol
            if quantity > 1:
                formula += str(quantity)
        return formula
    
