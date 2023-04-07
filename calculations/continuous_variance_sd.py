import sys

sys.path.append('../')
from calculus.integral import area_under_curve
from math import sqrt
def formula1(x):
    return x
def standard_deviation(f, start, end):

    expected_val = area_under_curve(f, 0.00001,end=end)
    print(expected_val)
    def d(x):
        return ((x - expected_val) **2) * f(1)

    variance = area_under_curve(d, 0.0001, start=start, end=end)
    print(variance)
    #
    # return {"expected value": expected_val,
    #         "variance": variance,
    #         "standard deviation": sqrt(variance)}

standard_deviation(formula1, start=0, end=1)