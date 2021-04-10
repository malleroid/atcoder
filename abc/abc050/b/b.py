import copy

N = int(input())
T = list(map(int, input().split()))
M = int(input())

for i in range(M):
    P, X = map(int, input().split())
    t = copy.deepcopy(T)
    t[P-1] = X
    print(sum(t))
