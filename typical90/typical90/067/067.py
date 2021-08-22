import numpy as np

N, K = map(int, input().split())

s = str(N)
for i in range(K):

    s = np.base_repr(int(s, 8), base=9)
    s = s.replace('8', '5')

print(s)
