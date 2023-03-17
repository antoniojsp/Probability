from random import randint

val = 100000

def test_monty_hall(times, switch):
    result = 0
    for _ in range(0, times):
        car_location = randint(0, 2)
        # player choose one (random since they have no information)
        player_choice = randint(0, 2)
        # now host pick one between the 2 lefts, he always picks the one with the goat and
        host_choice = [i for i in [0, 1, 2] if i not in [car_location, player_choice]][0]
        # try with player always changing door
        if switch:
            player_choice = [i for i in [0, 1, 2] if i not in [host_choice, player_choice]][0]

        if switch and car_location == player_choice:
            result += 1

    return result / times


print(test_monty_hall(10000, True))
