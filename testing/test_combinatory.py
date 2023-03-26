import sys

# sys.path.insert(0, '/Users/antonio/Documents/Probability/')
sys.path.insert(0, 'C:/Users/Antonio/PycharmProjects/Probability/calculations')
from calculations.combinatory import number_combinations
import math
import unittest


class TestCombinatory(unittest.TestCase):
    def test_combinatory(self):
        for i in [15, 13, 11, 9, 7, 5]:
            self.assertEqual(number_combinations(i, i - 2), math.comb(i, i - 2))

if __name__ == '__main__':
    unittest.main()