from calculations.m_standard_deviation import *

g_1 = [i for i in range(15,21)]
p_g_1 = [0.03, 0.07,0.17,0.28, 0.3, 0.15]
print(standard_deviation(g_1, p_g_1))
constant = 6
add_constant = list(map(lambda x: x + constant, g_1))
print(add_constant)
print(standard_deviation(add_constant, p_g_1))
