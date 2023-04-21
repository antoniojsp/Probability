

def factorial(num: int) -> int:
    '''
    Factorial of num
    time complexity 0(n)
    space complexty 0(1)
    :param num: int
    :return: factorial result
    '''
    if num == 0:
        return 1

    result = 1
    for i in range(2, num+1):
        result *= i
    return result


