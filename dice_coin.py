# Chances to get a 4 witha dice and heads (or tails) with a coin

from random import randrange
def dice(times:int, val:int)-> float:
    count = 0
    for _ in range(times):
         rand= randrange(0, 6)
         if rand == val:
            count +=1

    return count/times

def coin(times:int)-> float:
    suma = 0
    for _ in range(times):
        suma += randrange(0, 2)


    return suma/times


