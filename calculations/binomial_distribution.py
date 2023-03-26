from combinatory import number_combinations


def binomial_distr_formula(x: int, n: int, p: float) -> float:
    """
    :param x: variable
    :param n: total number ot trials
    :param p: probability of desire outcome
    :return: probability specific outcome
    """
    return number_combinations(n, x) * (p ** x) * (1 - p) ** (n - x)
