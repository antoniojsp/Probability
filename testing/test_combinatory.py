import sys
from os_detector import get_platform

platform = {"Win":'C:/Users/Antonio/PycharmProjects/Probability/calculations/',
            "OS":'/Users/antonio/Documents/Probability/calculations/'}

sys.path.insert(0, platform[get_platform()])

from combinatory import number_combinations
import math
import unittest


class TestCombinatory(unittest.TestCase):
    def test_combinatory(self):
        for i in [15, 13, 11, 9, 7, 5]:
            self.assertEqual(number_combinations(i, i - 2), math.comb(i, i - 2))

if __name__ == '__main__':
    unittest.main()