def fact(num:int):
	if num == 1:
		return 1
	return num * fact(num-1)

def fact_it(num:int):
	result = 1
	for i in range(1, num+1):
		result *= i

	return result



def number_combinations(total:int, chosen:int, f):
	return int(f(total)/(f(total - chosen) * f(chosen)))

# total 11
# chosen 3 (3,6,9)

print(number_combinations(15, 3, fact))
print(number_combinations(15, 1, fact))






