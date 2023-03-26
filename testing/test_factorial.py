import sys
sys.path.insert(0, '/Users/antonio/Documents/Probability/')

from calculations.factorial import factorial
import unittest


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        with open("fact_sample.txt", "r") as data:
            for i in data:
                items = i.split()
                self.assertEqual(factorial(int(items[0])), int(items[1]))
