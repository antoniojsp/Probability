from math import pi, sin, cos
import sys

sys.path.append('../')

from calculations.graph import graph


def area_under_curve(f, dx, end, start=0):
    area = 0
    i = start
    while i < end:
        area += dx * f(i)
        i += dx

    return area


def area_under_curve_graph(f, dx, end, start=0):
    area = 0
    i = start
    answer = []
    while i < end:
        area += dx * f(i)
        answer.append(dx * f(i))
        i += dx

    x_arr = [i for i in range(0, len(answer))]
    graph(x_arr, answer)
    return area


