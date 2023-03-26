import sys
sys.path.insert(0, '/Users/antonio/Documents/Probability/calculations')
from calculations.standard_deviation import standard_deviation

x = [-7, -4, -2, 1]
y = [0.16, 0.29, 0.09, 0.46]

print(standard_deviation(x, y))