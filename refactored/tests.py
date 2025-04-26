# tests/test_refactored_calculator.py
import unittest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import validate_numbers, addition, subtraction, multiplication, division, option


class TestRefactoredCalculator(unittest.TestCase):

    def test_options(self):
        # Test with invalid option
        self.assertEqual(option("5"), '0')

    def test_return(self):
        # Test with valid numbers
        self.assertEqual(addition("5", "7"), 12)
        self.assertEqual(subtraction("10", "7"), 3)
        self.assertEqual(multiplication("5", "7"), 35)
        self.assertEqual(division("10", "2"), 5)

        # Test with invalid first number
        self.assertEqual(addition("abc", "7"), '0')
        self.assertEqual(subtraction("abc", "7"), '0')
        self.assertEqual(multiplication("abc", "7"), '0')
        self.assertEqual(division("abc", "7"), '0')

        # Test with invalid second number
        self.assertEqual(addition("5", "xyz"), '0')
        self.assertEqual(subtraction("5", "xyz"), '0')
        self.assertEqual(multiplication("5", "xyz"), '0')
        self.assertEqual(division("5", "xyz"), '0')
        
    def test_validate_numbers(self):
        # Test with valid numbers
        is_valid, n1, n2 = validate_numbers("5", "7")
        self.assertTrue(is_valid)
        self.assertEqual(n1, 5.0)
        self.assertEqual(n2, 7.0)

        # Test with invalid first number
        is_valid, n1, n2 = validate_numbers("abc", "7")
        self.assertFalse(is_valid)

        # Test with invalid second number
        is_valid, n1, n2 = validate_numbers("5", "xyz")
        self.assertFalse(is_valid)

    def test_addition(self):
        # Test valid addition
        self.assertEqual(addition("5", "7"), 12)
        self.assertEqual(addition("-5", "7"), 2)
        self.assertEqual(addition("5.5", "7.5"), 13)

        # Test invalid input
        self.assertEqual(addition("abc", "7"), '0')

    def test_subtraction(self):
        # Test valid subtraction
        self.assertEqual(subtraction("10", "7"), 3)
        self.assertEqual(subtraction("-5", "7"), -12)
        self.assertEqual(subtraction("10.5", "7.5"), 3)

        # Test invalid input
        self.assertEqual(subtraction("abc", "7"), '0')

    def test_multiplication(self):
        # Test valid multiplication
        self.assertEqual(multiplication("5", "7"), 35)
        self.assertEqual(multiplication("-5", "7"), -35)
        self.assertEqual(multiplication("5.5", "2"), 11)

        # Test invalid input
        self.assertEqual(multiplication("abc", "7"), '0')

    def test_division(self):
        # Test valid division
        self.assertEqual(division("10", "2"), 5)
        self.assertEqual(division("-10", "2"), -5)
        self.assertEqual(division("10", "4"), 2.5)

        # Test division by zero
        self.assertEqual(division("10", "0"), '0')

        # Test invalid input
        self.assertEqual(division("abc", "7"), '0')


if __name__ == '__main__':
    unittest.main()