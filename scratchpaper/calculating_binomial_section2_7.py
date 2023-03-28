import sys
sys.path.append('../')

from calculations.binomial_distribution import binomial_distribution, binomial_distribution_cumulative

# all the seeds germinate
print(binomial_distribution(20,20, 0.9))
# at least 16
print(1 - binomial_distribution_cumulative(15,20, 0.9))
# at most 9
print("{0:.10f}".format(binomial_distribution_cumulative(9,20, 0.9)))
# more than 10 but less 16
more_10 = binomial_distribution_cumulative(10,20, 0.9)
less_16 = binomial_distribution_cumulative(14,20, 0.9)
print(less_16 - more_10)