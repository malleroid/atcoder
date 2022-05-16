import numpy as np

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

a = np.poly1d(A[::-1])
c = np.poly1d(C[::-1])

b = (c/a)

coefs = b[0].coef[::-1]
ans = np.array(coefs, dtype=int)

print(*ans, sep=" ")
