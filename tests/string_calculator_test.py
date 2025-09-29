import unittest
from src.string_calculator import string_calculator

class TestStringSum(unittest.TestCase):
    def test_two_valid_numbers(self):
        self.assertEqual(string_calculator("2", "3"), "5")

        def test_invalid_inputs(self):
            self.assertEqual(string_calculator("a", "3"), "3")
            self.assertEqual(string_calculator("2", "b"), "2")
            self.assertEqual(string_calculator("a", "b"), "0")
            self.assertEqual(string_calculator("", "3"), "3")
            self.assertEqual(string_calculator("2", ""), "2")
            self.assertEqual(string_calculator("", ""), "0")

    def test_large_numbers(self):
        self.assertEqual(string_calculator("12345678901234567890", "98765432109876543210"), "111111111011111111100")


if __name__ == '__main__':
    unittest.main()