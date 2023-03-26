from calculations.factorial import factorial
import unittest


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        with open("fact_sample.txt", "r") as data:
            for i in data:
                items = i.split()
                self.assertEqual(factorial(int(items[0])), int(items[1]))
