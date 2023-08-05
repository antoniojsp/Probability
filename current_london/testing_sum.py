arr_x = [1,3,2,4,10]

def sigma(f, lower, upper, arr)->float:
    result = 0
    for i in range(lower-1, upper):
        result += f(arr[i])
    return result

print("###RESULT###")
func_2 = lambda x: 2*(x**2)
print(sigma(func_2, 1, 3, arr_x))