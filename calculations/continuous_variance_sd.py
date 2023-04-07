import sys

sys.path.append('../')
from calculus.integral import area_under_curve
from math import sqrt


def standard_deviation(f, end, start=0):
    expected_val = area_under_curve(f, 0.00001, end=end, start=start)
    print(expected_val)

    def d(x):
        return ((x - expected_val) ** 2) * f(1)

    variance = area_under_curve(d, 0.0001, end=end, start=start)

    return {"expected value": expected_val,
            "variance": variance,
            "standard deviation": sqrt(variance)}


def standard_deviation2(f, f_2, end, start=0):
    expected_val = area_under_curve(f, 0.00001, end=end, start=start)
    e_x_2 = area_under_curve(f_2, 0.0001, end=end, start=start)
    return e_x_2 - expected_val ** 2


def formula_cereal(x):
    return x * (x / 200 - (39 / 20))


def formula_cereal2(x):
    return (x ** 2) * ((x ** 2) / 200 - (39 / 20))


def formula1(x):
    return x


def formula2(x):
    return x ** 2


# print(standard_deviation(formula1, 1, 0))
# print(standard_deviation2(formula1, formula2, 1, 0))
# print(standard_deviation2(formula1, formula2, 1, 0))
print(standard_deviation(formula_cereal, 410, 390))
