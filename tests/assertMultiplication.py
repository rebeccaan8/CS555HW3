import unittest
from calculator import multiplication


class TestMultiplication(unittest.TestCase):

    def test_multiplication_with_positive_numbers(self):
        self.assertEqual(multiplication("5", "7"), 35)

    def test_multiplication_with_negative_numbers(self):
        self.assertEqual(multiplication("-5", "-7"), 35)

    def test_multiplication_with_mixed_numbers(self):
        self.assertEqual(multiplication("-5", "7"), -35)
        self.assertEqual(multiplication("5", "-7"), -35)

    def test_multiplication_with_decimals(self):
        self.assertEqual(multiplication("5.5", "2"), 11)

    def test_multiplication_with_zero(self):
        self.assertEqual(multiplication("0", "7"), 0)
        self.assertEqual(multiplication("5", "0"), 0)

    def test_multiplication_with_invalid_input(self):
        # Test with invalid input (this will print an error message, but we're testing the return value)
        self.assertEqual(multiplication("abc", "7"), '0')
        self.assertEqual(multiplication("5", "xyz"), '0')


if __name__ == '__main__':
    unittest.main()