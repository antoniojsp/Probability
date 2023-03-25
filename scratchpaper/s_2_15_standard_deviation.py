from m_standard_deviation import standard_deviation, expected_value
from math import sqrt


g_1 = [i for i in range(15,21)]
p_g_1 = [0.03, 0.07,0.17,0.28, 0.3, 0.15]
print(standard_deviation(g_1, p_g_1))
#
g_1 = [i for i in range(15,21)]
p_g_1 = [0.11, 0.15, 0.23, 0.27, 0.18, 0.06]
print(standard_deviation(g_1, p_g_1))



# g_1 = [i**2 for i in range(15,21)]
# print(g_1)
# part1 = expected_value(g_1, p_g_1)
# g_1 = [i for i in range(15,21)]
# g2 = map(lambda x: x**2, g_1)
# print(list(g2))
#
# part2 = standard_deviation(g2, p_g_1)["standard deviation"]**2
# result = part1 - part2
# print(sqrt(result))
