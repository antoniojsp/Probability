with open("data.txt") as my_file:
    temp = my_file.readlines()
    result = [i.split() for i in temp]
    clients = {i[0]: int(i[1]) + int(i[2]) for i in result}

# 1st question, 7 clients
condition = 7
resultado = 0
for i in clients.values():
    if i == condition:
        resultado += 1
print(resultado/len(clients))

# 2
cat = [i[1] for i in result]
dog = [i[2] for i in result]

def prob_table(arr: list):
    dict_result = {}
    for i in arr:
        if i not in dict_result:
            dict_result[i] = round(1 / len(arr), 2)
        else:
            dict_result[i] += round(1 / len(arr), 2)

    return dict(sorted(dict_result.items()))

print(prob_table(clients.values()))
