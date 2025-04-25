import unittest
from calculator import addition, subtraction, multiplication, division


class TestNumberValidation(unittest.TestCase):

    def test_valid_numbers_produce_results(self):
        # Test that valid numbers produce numerical results
        self.assertEqual(addition("5", "7"), 12)
        self.assertEqual(subtraction("10", "7"), 3)
        self.assertEqual(multiplication("5", "7"), 35)
        self.assertEqual(division("10", "2"), 5)

    def test_invalid_first_number(self):
        # Test that invalid first number returns '0'
        self.assertEqual(addition("abc", "7"), '0')
        self.assertEqual(subtraction("abc", "7"), '0')
        self.assertEqual(multiplication("abc", "7"), '0')
        self.assertEqual(division("abc", "7"), '0')

    def test_invalid_second_number(self):
        # Test that invalid second number returns '0'
        self.assertEqual(addition("5", "xyz"), '0')
        self.assertEqual(subtraction("5", "xyz"), '0')
        self.assertEqual(multiplication("5", "xyz"), '0')
        self.assertEqual(division("5", "xyz"), '0')

    def test_division_by_zero(self):
        # Test that division by zero returns '0'
        self.assertEqual(division("10", "0"), '0')


if __name__ == '__main__':
    unittest.main()