"""
test_factorial.py

Unit tests for the recursive factorial() function.
Run with:  python -m unittest test_factorial.py -v
"""

import unittest
from factorial import factorial


class TestFactorial(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_small_numbers(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    def test_larger_number(self):
        self.assertEqual(factorial(10), 3628800)

    def test_recursion_depth_reasonable_input(self):
        # Sanity check for a moderately large value
        self.assertEqual(factorial(15), 1307674368000)


if __name__ == "__main__":
    unittest.main()
