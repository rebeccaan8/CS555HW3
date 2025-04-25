import unittest
from calculator import option

class TestCalculatorOptions(unittest.TestCase):
    def test_invalid_option(self):
        # Test invalid operation choices
        self.assertIsNone(option("5"))  # Invalid option number
        self.assertIsNone(option("0"))  # Out of range option
        self.assertIsNone(option("abc"))  # Non-numeric option
        self.assertIsNone(option(""))  # Empty input
        self.assertIsNone(option(" "))  # Whitespace only
        
    def test_option_bounds(self):
        # Test boundary values
        self.assertIsNone(option("-1"))  # Negative number
        self.assertIsNone(option("1.5"))  # Decimal number
        self.assertIsNone(option("10"))  # Number > 4

    def test_special_characters(self):
        # Test special character inputs
        self.assertIsNone(option("!"))  # Special character
        self.assertIsNone(option("1+"))  # Number with special char
        self.assertIsNone(option("\n"))  # Newline character
        self.assertIsNone(option("\t"))  # Tab character

    def test_malformed_inputs(self):
        # Test malformed inputs
        self.assertIsNone(option("1,2"))  # Comma in number
        self.assertIsNone(option("1.0.0"))  # Multiple decimal points
        self.assertIsNone(option("1e10"))  # Scientific notation
        self.assertIsNone(option("True"))  # Boolean value
        self.assertIsNone(option("None"))  # None value
        
        
    def test_leading_trailing_spaces(self):
        # Test inputs with various spacing
        self.assertIsNone(option(" 1"))  # Leading space
        self.assertIsNone(option("1 "))  # Trailing space
        self.assertIsNone(option(" 1 "))  # Both leading and trailing space
        self.assertIsNone(option("1\n"))  # Trailing newline

if __name__ == '__main__':
    unittest.main()
