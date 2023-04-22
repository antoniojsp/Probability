import sys

sys.path.append('../')
from harvard110.combinatory import comb_reduce
from math import factorial

# problem a1
print(comb_reduce(12, 2) * comb_reduce(10, 5) // 2)

# problem a2
print(comb_reduce(12, 4) * comb_reduce(8, 4) * comb_reduce(4, 4) // factorial(3))
