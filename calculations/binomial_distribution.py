from combinatory import number_combinations
def binomial_distr_formula(x, n, p):
    """
    :param x: variable
    :param n: total
    :param p: probability
    :return: probability specific outcome
    """
    return number_combinations(n, x) * (p ** x) * (1 - p) ** (n - x)
