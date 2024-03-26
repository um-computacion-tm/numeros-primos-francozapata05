import unittest

def is_primo(value):
    
    cont = value
    contP = 0

    if value > 3:
        for i in range(value,1,-1):
            if value%cont == 0:
                contP = contP + 1
                cont = cont - 1
            else:
                cont = cont - 1
        
        if contP == 1:
            return True
        else:
            return False
    
    if value <=0:
        return False

    else:
        return True

class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, True)

    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)
    
    
    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)

    
    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)
    
    
    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)

    def test_6(self):
        result = is_primo(6)
        self.assertEqual(result, False)

unittest.main()  