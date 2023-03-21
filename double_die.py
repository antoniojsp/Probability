from random import randint, choice


def roll_die_probability(times: int):
    dic_result = {}
    for i in range(times):
        outcome = randint(1, 6)
        if outcome not in dic_result:
            dic_result[outcome] = 0
        dic_result[outcome] += 1 / times

    return dict(sorted(dic_result.items()))


# print(roll_die_probability(100000))

def roll_two_die_probability(times: int, choice1: list, choice2: list):
    dic_result = {}
    for i in range(times):
        suma = choice(choice1) + choice(choice2)
        if suma not in dic_result:
            dic_result[suma] = 0
        dic_result[suma] += 1 / times

    return dict(sorted(dic_result.items()))


def n_dice(number_dice: int, times: int)->dict:
    results = {}
    for i in range(times):
        total_result = 0
        for j in range(number_dice):
            total_result += randint(1, 6)
        if total_result not in results:
            results[total_result] = 0
        results[total_result] += 1 / times

    return dict(sorted(results.items()))


prob = n_dice(6, 10000000)

import matplotlib.pyplot as plt

x = [i for i in range(len(prob))]
y = list(prob.values())
plt.bar(x, y, align='center')  # A bar chart
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.show()
