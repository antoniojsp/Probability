# (a and not b) or (not a and b)

a = True
b = False

xor = lambda x, y: (x and not y) or (not x and y)

print(xor(a, b))