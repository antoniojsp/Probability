def expected_value(random_var: list, probability_arr: list) -> float:
    '''
    Expected value, multiply the random variables by their probabilities
    and then get it's mean.
    :param random_var:
    :param probability_arr:
    :return:
    '''
    result = 0
    for i, j in zip(random_var, probability_arr):
        result += i * j

    return result
