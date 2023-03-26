import sys

sys.path.insert(0, '/Users/antonio/Documents/Probability/calculations')

from calculations.binomial_distribution import binomial_distr_formula
from calculations.graph import graph

times = 5
x = [i for i in range(0, times + 1)]
y = [binomial_distr_formula(i, times, 0.5) for i in range(times + 1)]
print(y)
graph(x, y)
