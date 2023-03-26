import sys

sys.path.insert(0, '/Users/antonio/Documents/Probability/calculations')

from factorial import factorial


def number_combinations(total: int, chosen: int) -> int:
    return int(factorial(total) / (factorial(total - chosen) * factorial(chosen)))
