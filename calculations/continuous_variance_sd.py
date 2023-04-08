import sys

sys.path.append('../')
from calculus.integral import area_under_curve
from calculations.expected_value import expected_value_continuous
from math import sqrt


def standard_deviation(f, end, start=0):
    expected_val = expected_value_continuous(f, end, start)
    d = lambda x:((x - expected_val) ** 2) * f(x)
    variance = area_under_curve(d, 0.0001, end=end, start=start)

    return {"expected value": expected_val,
            "variance": variance,
            "standard deviation": sqrt(variance)}


def standard_deviation2(f, end, start=0):
    expected_val = expected_value_continuous(f, end, start)
    f_2 = lambda x: x**2 * f(x)
    expected_val_square = area_under_curve(f_2, 0.0001, end=end, start=start)
    return sqrt(expected_val_square - (expected_val ** 2))


