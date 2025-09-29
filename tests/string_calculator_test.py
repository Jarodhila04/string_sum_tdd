import unittest
from src.string_calculator import string_calculator

class TestStringSum(unittest.TestCase):
    def test_two_valid_numbers(self):
        self.assertEqual(string_calculator("2", "3"), "5")