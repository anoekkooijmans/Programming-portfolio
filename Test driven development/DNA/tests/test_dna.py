import pytest
from bin.dna import DNA

def test_init_valid_sequence():
    # Positive test for initializing DNA object with a valid sequence
    sequence = 'ACTGACTGACTG'
    dna = DNA(sequence)
    assert dna.sequence == sequence

def test_init_invalid_sequence_type():
    # Negative test for initializing DNA object with invalid sequence type
    with pytest.raises(TypeError):
        DNA(123)

def test_init_invalid_nucleotides():
    # Negative test for initializing DNA object with invalid nucleotides
    with pytest.raises(ValueError):
        DNA('ACTGXACTGACTG')

def test_init_invalid_length():
    # Negative test for initializing DNA object with invalid sequence length
    with pytest.raises(ValueError):
        DNA('ACTGACT')

def test_print_dna():
    # Positive test for printing DNA object
    dna = DNA('ACTGACTGACTG')
    assert str(dna) == 'ACTGACTGACTG'

def test_add_triplet():
    # Positive test for adding a triplet to DNA object
    dna = DNA('ACTGACTGACTG')
    new_dna = dna + 'ACG'
    assert new_dna.sequence == 'ACTGACTGACTGACG'

def test_iteration():
    # Positive test for iterating over DNA object
    dna = DNA('ACTGACTGACTG')
    triplets = [triplet for triplet in dna]
    assert triplets == ['ACT', 'GAC', 'TGA', 'CTG']

def test_immutable():
    # Negative test for modifying DNA object
    dna = DNA('ACTGACTGACTG')
    with pytest.raises(AttributeError):
        dna.sequence = 'ACGTACGTACGT'
