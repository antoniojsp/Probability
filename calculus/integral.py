from math import pi, sin
import sys

sys.path.append('../')

from calculations.graph import graph


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


def area_under_curve(f, dx, end, start=0):
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
# print(area_under_curve(continuous_function1, 0.00001, 410, 404))
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()