import sys

sys.path.append('../')

from calculations.binomial_distribution import binomial_distribution, binomial_distribution_cumulative

times = 17

y =  binomial_distribution(5, times, 0.26)
print(y)



y =  binomial_distribution_cumulative(4, times, 0.26)
print(y)

print(17*0.26)