from factorial import factorial


def number_combinations(total: int, chosen: int):
    return int(factorial(total) / (factorial(total - chosen) * factorial(chosen)))



