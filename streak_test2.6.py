
f = lambda x: (x, (x**2) - (2*x) + 10)
values = [-2,-1,0,1,2,3]

temp = dict(map(f, values))
print(temp)