import sys

sys.path.append('../')

from calculations.binomial_distribution import binomial_distribution
from calculations.graph import graph

times = 20
x = [i for i in range(0, times + 1)]
y = [binomial_distribution(i, times, 0.5) for i in range(times + 1)]
print(y)
graph(x, y)
