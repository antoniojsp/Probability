arr_x = [7,3,1,0,-6]
arr_y = [-3, 5,-8, 9, 1]
func = lambda x: 2*x

def sigma(f, lower, upper, arr, arr_used)->float:
    result = 0
    for i in range(lower-1, upper):
        print(arr[i])
        result += f(arr[i])

    return result

print("###RESULT###")
func_2 = lambda x: 4*(x-1)
func_3 = lambda x, y: x**2+2*(y**2)
arr_used = [arr_y, arr_x]
print(sigma(func_3, 1, 3, arr_used))