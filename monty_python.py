from random import randint

val = 10000

def test_monty_hall(times:int, switch=True):
    result = 0
    lista = []
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
            lista.append(1)
            result +=1
        if switch and car_location !=player_choice:
            lista.append(0)

    return result / times
    # return lista

print(test_monty_hall(val, True))


game_times = [i for i in range(1, 2000)]
temp = []
for i in game_times:
    temp.append(test_monty_hall(i))

print(temp)
import matplotlib.pyplot as plt
# x axis values
x = [i for i in range(len(temp))]
# corresponding y axis values
y = temp
# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth=1,
         marker='o', markerfacecolor='blue', markersize=1)
# setting x and y axis range
plt.ylim(0.5, 0.8)
plt.xlim(0, len(temp))
# naming the x axis
plt.xlabel('Number of times')
# naming the y axis
plt.ylabel('Percentage of win if switching')

# giving a title to my graph
plt.title('Monty Hall problem')

# function to show the plot
plt.show()