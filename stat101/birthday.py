group_size = 23


def prob_not_same_day_birthday(k: int)->float:
    '''
    Gets first the probability that event doesn't happen and then substract 1 to obtain the probability an eveng
    actually does happen.
    :param k:
    :return:
    '''
    days_in_year = 365
    answer = 1
    for i in range(days_in_year, days_in_year - k, -1):
        answer *= i
    result = answer / (days_in_year ** k)

    return 1 - result


for i in range(1, 366):
    print(i, prob_not_same_day_birthday(i))
