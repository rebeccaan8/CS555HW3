import unittest
from refactored.calculator import addition, subtraction, multiplication, division

class TestReturnValues(unittest.TestCase):

    def check_result(self, func, a, b, expected):
        result = func(a, b)
        self.assertEqual(result, expected, f"{func.__name__}({a}, {b}) returned {result}, expected {expected}")
        self.assertIsInstance(result, (int, float), f"{func.__name__} returned {type(result)} instead of number")

    def test_addition(self):
        self.check_result(addition, "2", "3", 5)

    def test_subtraction(self):
        self.check_result(subtraction, "10", "4", 6)

    def test_multiplication(self):
        self.check_result(multiplication, "2", "3", 6)

    def test_division(self):
        self.check_result(division, "10", "2", 5)

    def test_addition_invalid_input(self):
        self.assertEqual(addition("a", "2"), 0)
        self.assertEqual(addition("5", "b"), 0)

    def test_division_by_zero(self):
        self.assertEqual(division("10", "0"), 0)
        self.assertEqual(division("0", "0"), 0)

if __name__ == '__main__':
    unittest.main()
