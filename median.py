test = [0.18, 0.16, 0.03, 0.44, 0.01, 0.03, 0.09, 0.06]
test.reverse()
suma = 0
for i in test:
    suma += i
    print(i)
    if suma > 0.5:
        break