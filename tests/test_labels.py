import unittest
from labels import get_label


class TestStringMethods(unittest.TestCase):
    def test_less10(self):
        self.assertEqual(get_label(1), 1)

    def test_more10(self):
        self.assertEqual(get_label(19), 10)

    def test_more1000(self):
        self.assertEqual(get_label(1111), 4)

    def test_negative(self):
        self.assertRaises(AssertionError, get_label, -1)

    def test_number(self):
        self.assertRaises(AssertionError, get_label, "omg")


if __name__ == "__main__":
    unittest.main()
