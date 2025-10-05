import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        # tests the add function in simple_calculator
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(8, 3), 5)

    def test_divide(self):
        self.assertEqual(self.calc.divide(12, 3), 4)
        self.assertEqual(self.calc.divide(5, 0), None)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(3, 3), 9)


if __name__ == "__main__":
    unittest.main()
