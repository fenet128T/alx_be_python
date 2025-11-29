
import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(5, 7), 12)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-5, -8), -13)
        self.assertEqual(self.calc.add(-10, -20), -30)

    def test_addition_mixed_signs(self):
        self.assertEqual(self.calc.add(-5, 8), 3)
        self.assertEqual(self.calc.add(10, -7), 3)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_floats(self):
        self.assertAlmostEqual(self.calc.add(1.5, 2.7), 4.2)
        self.assertAlmostEqual(self.calc.add(-1.1, 0.1), -1.0)

    # Tests for subtraction
    def test_subtraction_positive(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(100, 50), 50)

    def test_subtraction_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_subtraction_with_negatives(self):
        self.assertEqual(self.calc.subtract(-5, -8), 3)
        self.assertEqual(self.calc.subtract(-10, 5), -15)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_subtraction_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.3), 3.2)
        self.assertAlmostEqual(self.calc.subtract(1.0, 0.9), 0.1)

    # Tests for multiplication
    def test_multiplication_basic(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(5, -4), -20)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 15), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiplication_negatives(self):
        self.assertEqual(self.calc.multiply(-3, -5), 15)
        self.assertEqual(self.calc.multiply(-6, 4), -24)

    def test_multiplication_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calc.multiply(1.5, 0.1), 0.15)

    # Tests for division
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)

    def test_division_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-15, -3), 5.0)

    def test_division_with_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), -0.0)  # Note: -0.0 == 0.0 in Python

    def test_division_floats(self):
        self.assertAlmostEqual(self.calc.divide(5.0, 2), 2.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333)


if __name__ == "__main__":
    unittest.main(verbosity=2)