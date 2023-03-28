import sys
sys.path.append('../')

from calculations.combinatory import number_combinations


def binomial_distribution(x: int, n: int, p: float) -> float:
    """
    :param x: variable
    :param n: total number ot trials
    :param p: probability of desire outcome
    :return: probability specific outcome
    """

    return number_combinations(n, x) * (p ** x) * (1 - p) ** (n - x)


def binomial_distribution_cumulative(x: int, n: int, p: float):
    """
    Return the cumulative probability i.e P(x>=4)
    :param x: variable
    :param n: total number ot trials
    :param p: probability of desire outcome
    :return: probability specific outcome
    """
    cumulative = 0
    for i in range(0, x + 1):
        print(cumulative)
        cumulative += binomial_distribution(i, n, p)

    return cumulative


