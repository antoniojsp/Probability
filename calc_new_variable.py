# https://learning.edx.org/course/course-v1:AdelaideX+ProbTraX+1T2020/block-v1:AdelaideX+ProbTraX+1T2020+type@sequential+block@a80ceb2b23164e899550c3aa50eb1398/block-v1:AdelaideX+ProbTraX+1T2020+type@vertical+block@cb495106c252468ab4447a80a7ed3e94

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 1, 2, 3, 4 ])
ypoints = np.array([0.2, 0.1, 0.35, 0.1, 0.25])


xpoints1 = np.array([-2, 0, 4])
ypoints1 = np.array([0.45, 0.3, 0.25])


plt.plot(xpoints,ypoints,'-o',color='b')
plt.plot(xpoints1,ypoints1,'-x',color='r')

plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()