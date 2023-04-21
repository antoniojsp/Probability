
import sys
sys.path.append('../')
from harvard110.factorial import factorial as fact
import unittest
from math import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        for i in range(10000):
            assert factorial(i) == fact(i)

if __name__ == '__main__':
    unittest.main()
