from bin.summing import simple_sum, multiple_sum

def test_sum():
    assert simple_sum(3,3) == 6, 'should be 6'

def test_another_sum():
    assert multiple_sum(1,2,3,4,5) == 15