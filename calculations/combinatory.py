import sys
sys.path.append('../')
from calculations.factorial import factorial


def number_combinations(total: int, chosen: int) -> int:
    return int(factorial(total) / (factorial(total - chosen) * factorial(chosen)))
