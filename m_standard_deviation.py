from math import sqrt

def expected_value(random_var:list, probability_arr:list):
    result = 0
    for i, j in zip(random_var, probability_arr):
        result += i*j

    return result

def standard_deviation(random_var:list, prob_arr:list) -> dict:
    '''
    Long version to calculate standard deviation
    shorter:
    variance = e(x^2) - e(x)^2
    standard deviation is the square root of the variance

    :param random_var:list of random variables
    :param prob_arr: list of probabilities
    :return: dictionary with expected value, variance and s. deviation
    '''
    expected_val = expected_value(random_var, prob_arr)
    result = 0
    for var, prob in zip(random_var, prob_arr):
        result += ((var - expected_val)**2)*prob

    return {"expected value":expected_val,
            "variance":result,
            "standard deviation": sqrt(result)}
