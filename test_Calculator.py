import unittest
from Calculator import Calculator

class CalculatorTest(unittest.TestCase):
    calculator = Calculator()
    def test_add(self):
        self.assertEqual( self.calculator.add())

if __name__ == "__main__":
    unittest.main()
