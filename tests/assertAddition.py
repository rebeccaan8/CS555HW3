import unittest
from calculator import addition


class TestAddition(unittest.TestCase):

    def test_addition_with_positive_numbers(self):
        self.assertEqual(addition("5", "7"), 12)

    def test_addition_with_negative_numbers(self):
        self.assertEqual(addition("-5", "-7"), -12)

    def test_addition_with_mixed_numbers(self):
        self.assertEqual(addition("-5", "7"), 2)

    def test_addition_with_decimals(self):
        self.assertEqual(addition("5.5", "7.25"), 12.75)

    def test_addition_with_zero(self):
        self.assertEqual(addition("0", "7"), 7)
        self.assertEqual(addition("5", "0"), 5)

    def test_addition_with_invalid_input(self):
        # Test with invalid input (this will print an error message, but we're testing the return value)
        self.assertEqual(addition("abc", "7"), '0')
        self.assertEqual(addition("5", "xyz"), '0')


if __name__ == '__main__':
    unittest.main()