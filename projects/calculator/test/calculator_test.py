import unittest

from projects.calculator.src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 2)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()