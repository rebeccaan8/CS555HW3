import unittest
from calculator import subtraction


class TestSubtraction(unittest.TestCase):

    def test_subtraction_with_positive_numbers(self):
        self.assertEqual(subtraction("10", "7"), 3)

    def test_subtraction_with_negative_numbers(self):
        self.assertEqual(subtraction("-5", "-7"), 2)

    def test_subtraction_with_mixed_numbers(self):
        self.assertEqual(subtraction("-5", "7"), -12)
        self.assertEqual(subtraction("5", "-7"), 12)

    def test_subtraction_with_decimals(self):
        self.assertEqual(subtraction("10.5", "7.25"), 3.25)

    def test_subtraction_with_zero(self):
        self.assertEqual(subtraction("0", "7"), -7)
        self.assertEqual(subtraction("5", "0"), 5)

    def test_subtraction_with_invalid_input(self):
        # Test with invalid input (this will print an error message, but we're testing the return value)
        self.assertEqual(subtraction("abc", "7"), '0')
        self.assertEqual(subtraction("5", "xyz"), '0')


if __name__ == '__main__':
    unittest.main()