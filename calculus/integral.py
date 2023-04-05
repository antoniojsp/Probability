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

# print(area_under_curve(inverse_parabola, 1.414, 0.00001))
# print(area_under_curve(formula_cereal, 0.00001, 410, 390))
# import matplotlib.pyplot as plt
# import numpy as np
#
# plt.style.use('_mpl-gallery')
#
# # make data
# x = np.linspace(0, 10, 100)
# y = 4 + 2 * np.sin(2 * x)
#
# # plot
# fig, ax = plt.subplots()
#
# ax.plot(x, y, linewidth=2.0)
#
# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))
#
# plt.show()
