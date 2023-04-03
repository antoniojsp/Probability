# formula = x**2
from math import pi


def perimeter_circle(r):
    return 2 * pi * r


def parabola(x):
    return x ** 2


def inverse_parabola(x):
    return -1*(x**2) + 2


def integral_parabola(end, start=0):
    return (end ** 3) / 3 - (start ** 3) / 3


def area_under_curve(f, end, dx):
    area = 0
    i = 0
    while i < end:
        area += dx * f(i)
        i += dx

    return area


print(area_under_curve(inverse_parabola, 1.414, 0.00001))
