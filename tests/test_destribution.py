import unittest
from destribution import get_destributions_from_zero, get_destributions


class TestStringMethods(unittest.TestCase):
    def test_less10(self):
        self.assertEqual(get_destributions_from_zero(11)[0], ('1', 2))
        
    def test_more10(self):
        self.assertEqual(get_destributions_from_zero(195)[0], ('9', 19))
        
    def test_more1000(self):
        self.assertEqual(get_destributions_from_zero(1678)[0], ('13', 133))
        
    def test_negative(self):
        self.assertRaises(AssertionError, get_destributions_from_zero, -1)
        
        
            
        
    def test_less10(self):
        self.assertEqual(get_destributions(9, 8)[0], ('9', 1))
        
    def test_more10(self):
        self.assertEqual(get_destributions(195, 265)[0], ('11', 25))
        
    def test_more1000(self):
        self.assertEqual(get_destributions(1678, 2564)[0], ('16', 194))
        
    def test_negative(self):
        self.assertRaises(AssertionError, get_destributions, -1, -2)
        
        

if __name__ == "__main__":
    unittest.main()
