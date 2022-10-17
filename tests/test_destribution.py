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
        
    def test_number(self):
        self.assertRaises(AssertionError, get_destributions_from_zero, "omg")
        
    


if __name__ == "__main__":
    unittest.main()
