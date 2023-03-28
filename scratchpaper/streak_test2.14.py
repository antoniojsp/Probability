import sys
sys.path.append('../')

from calculations.binomial_distribution import binomial_distribution, binomial_distribution_cumulative

 # p(x=2)
print(binomial_distribution(2, 6,0.35))
# p(x>=2) =
print(1-binomial_distribution_cumulative(1, 6, 0.35))