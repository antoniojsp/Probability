import sys

sys.path.append('../')
from calculations.continuous_variance_sd import standard_deviation2, standard_deviation

def formula_cereal(x):
    return x / 200 - (39 / 20)
# print(standard_deviation(formula_cereal, 410, 390))


def formula_cereal2(x):
    return (x ** 2) * (x  / 200 - (39 / 20))


a = lambda x: (1000/333)*(x**-4)
# print(standard_deviation(formula_cereal, 410, 390))
print(standard_deviation2(a, 10,1))
# print(standard_deviation2(lambda x: 1, 1))