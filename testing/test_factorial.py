import sys
from os_detector import get_platform

platform = {"Win":'C:/Users/Antonio/PycharmProjects/Probability/',
            "OS":'/Users/antonio/Documents/Probability/calculations'}

sys.path.insert(0, platform[get_platform()])

from factorial import factorial
import unittest


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        with open("fact_sample.txt", "r") as data:
            for i in data:
                items = i.split()
                self.assertEqual(factorial(int(items[0])), int(items[1]))

if __name__ == '__main__':
    unittest.main()