import sys

sys.path.append('../')
from calculus.integral import area_under_curve
from math import sin, cos, pi


def perimeter_circle(r):
    return 2 * pi * r


def parabola(x):
    return x ** 2


def inverse_parabola(x):
    return -1 * (x ** 2) + 2


def integral_parabola(end, start=0):
    return (end ** 3) / 3 - (start ** 3) / 3


def continuous_function1(x):
    return (x / 200) - (39 / 20)


def formula2(x):
    return 1 / 6 * x + 1 / 3


def formula_cereal(x):
    return (x ** 2) / 200 - (39 / 20) * x


# print(area_under_curve(formula_cereal, 0.00001, 410, 390))
