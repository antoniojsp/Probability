import sys

sys.path.append('../')
from harvard110.combinatory import comb_reduce
import math
import unittest


class TestCombinatory(unittest.TestCase):
    def test_combinatory(self):
        for i in [1500, 13000, 110000, 900, 70, 50000]:
            self.assertEqual(comb_reduce(i, i - 2), math.comb(i, i - 2))


if __name__ == '__main__':
    unittest.main()
