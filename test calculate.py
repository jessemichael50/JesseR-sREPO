from calculate import square

def main():
    test_square()
   

def test_square():
    assert square(3) == 9
    assert square(0) == 0
    assert square(-3) == 9
    assert square(4) == 16
    assert square(2) == 4