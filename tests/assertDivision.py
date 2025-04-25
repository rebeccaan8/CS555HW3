import unittest

from calculator import division


class TestDivision(unittest.TestCase):

    def test_division_with_positive_numbers(self):
        self.assertEqual(division("10", "2"), 5)

    def test_division_with_negative_numbers(self):
        self.assertEqual(division("-10", "-2"), 5)

    def test_division_with_mixed_numbers(self):
        self.assertEqual(division("-10", "2"), -5)
        self.assertEqual(division("10", "-2"), -5)

    def test_division_with_decimals(self):
        self.assertEqual(division("10", "4"), 2.5)

    def test_division_with_dividend_zero(self):
        self.assertEqual(division("0", "7"), 0)

    def test_division_by_zero(self):
        # Test division by zero (this will print an error message, but we're testing the return value)
        self.assertEqual(division("10", "0"), '0')

    def test_division_with_invalid_input(self):
        # Test with invalid input (this will print an error message, but we're testing the return value)
        self.assertEqual(division("abc", "7"), '0')
        self.assertEqual(division("5", "xyz"), '0')


if __name__ == '__main__':
    unittest.main()