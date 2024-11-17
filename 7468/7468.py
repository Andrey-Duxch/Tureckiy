from math import *
N = 10 + 26 + 8164
i = ceil(log2(N))
numbers = 835
I = 156 * 1024
k_list = []
for k in range(1,1000):
    if ceil(k*i/8) * numbers > I:
        k_list.append(k)
print(k_list)
#ответ 110