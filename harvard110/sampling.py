sampling_replacement = lambda n, k: n ** k


def sampling_no_replacement(n, k):
    result = 1
    for i in range(n, n - k, -1):
        result *= i
        #divide to eliminate the duplicates
    return int(result/k)


# print(f"{1 - sampling_no_replacement(365, 5)/(365**5):,}")
print(sampling_no_replacement(4, 2))