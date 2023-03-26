#https://learning.edx.org/course/course-v1:AdelaideX+ProbTraX+1T2020/block-v1:AdelaideX+ProbTraX+1T2020+type@sequential+block@944a74e8448f4ab3bd0f4e917b81981f/block-v1:AdelaideX+ProbTraX+1T2020+type@vertical+block@a38225a9993945be95cfee0ac0eebf5a

from random import choice

times = 100000
result = {}
for i in range(times):
    a = choice([0,1,2,2,3,3])
    b = choice([0,0,0,0,0,6])

    if a + b not in result:
        result[a+b] = 0
    result[a+b] += 1/times

resultado = 0
for i, j in result.items():
    resultado +=  int(i)*j

print(resultado)


