from math import sqrt

def expected_value(random_var:list, probability_arr:list):
    '''
    Expected value, multiply the random variables by their probabilities
    and then get it's mean.
    :param random_var:
    :param probability_arr:
    :return:
    '''
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
    if len(random_var) != len(prob_arr):
        return {"error":"list size mismatch"}

    expected_val = expected_value(random_var, prob_arr)
    variance = 0
    for variable, prob in zip(random_var, prob_arr):
        variance += ((variable - expected_val)**2)*prob

    return {"expected value":expected_val,
            "variance":variance,
            "standard deviation": sqrt(variance)}
