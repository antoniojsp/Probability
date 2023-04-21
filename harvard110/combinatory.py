from math import factorial


def factorial_limit(n, limit):
    result = 1
    for i in range(limit + 1, n + 1):
        result *= i
    return result


comb_formula = lambda n, k: factorial(n) // (factorial(k) * factorial(n - k))

comb_reduce = lambda n, k: factorial_limit(n, n - k) // factorial(k)

