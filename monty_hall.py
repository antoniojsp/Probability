from random import randint


def exclude_elements(length: int, excluded: list):
    '''
    Given a length of range [0...length] and a excluded list of items, return the element from range not
    in the excluded list. The elements in the range need to be one more than the excluded list.
    :param length: range length
    :param excluded: list of items that need to be excluded from the range
    :return: returns the only element from range that is not included in the excluded list
    '''

    all_options = set(range(length))
    exclusion_list = set(excluded)
    return (all_options - exclusion_list).pop()


def test_monty_hall(game) -> dict:
    won = 0
    lost = 0
    times = game.number_times()
    NUMBER_DOORS = 3
    for _ in range(0, times):
        car_location = randint(0, NUMBER_DOORS - 1)
        # player choose one (random since they have no information)
        player_choice = randint(0, NUMBER_DOORS - 1)
        # now host pick one between the 2 lefts, he always picks the one with the goat and
        host_choice = exclude_elements(NUMBER_DOORS, [car_location, player_choice])
        # try with player always changing door
        if game.is_switching_door():
            player_choice = exclude_elements(NUMBER_DOORS, [host_choice, player_choice])

        if car_location == player_choice:  #
            won += 1
        else:
            lost += 1

    return {"won": won / times, "lost": lost / times}


class MontyHallGame:
    def __init__(self, times: int, switching_door: bool):
        self.times = times
        self.switching_door = switching_door

    def is_switching_door(self):
        return self.switching_door

    def number_times(self):
        return self.times


N_TIMES = 100000
game = MontyHallGame(times=N_TIMES, switching_door=True)
answer_switch = test_monty_hall(game)
print(f"If the user switch doors, they win {answer_switch['won']:.2f} % times and lose {answer_switch['lost']:.2f}")
