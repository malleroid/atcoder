import numpy as np

n = int(input())

a = list(map(int, input().split()))


res = np.prod(a)
print(type(res))
if res > 10**18 :
    print(-1)

else:
    print(res)