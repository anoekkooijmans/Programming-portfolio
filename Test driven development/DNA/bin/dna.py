class DNA:
    def __init__(self, sequence):
        if not isinstance(sequence, str):
            raise TypeError("DNA sequence must be a string")

        valid_nucleotides = set('ACTG')
        if not set(sequence).issubset(valid_nucleotides):
            raise ValueError("DNA sequence can only contain characters A, C, T, G")

        if len(sequence) % 3 != 0:
            raise ValueError("DNA sequence length must be a multiple of three")

        self._sequence = sequence  # Use a private attribute

    @property
    
    def sequence(self):
        return self._sequence

    def __str__(self):
        return self.sequence

    def __add__(self, other):
        if not isinstance(other, str) or len(other) != 3:
            raise ValueError("Invalid triplet to add to DNA sequence")

        valid_nucleotides = set('ACTG')
        if not set(other).issubset(valid_nucleotides):
            raise ValueError("Triplet can only contain characters A, C, T, G")

        return DNA(self.sequence + other)

    def __iter__(self):
        return iter([self.sequence[i:i + 3] for i in range(0, len(self.sequence), 3)]) 

    
dna = DNA('ACTGACTGACTG')
for triplet in dna:
    print(triplet)
