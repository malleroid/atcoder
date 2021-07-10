import copy

N = int(input())
X = list(map(int, input().split()))

x = copy.deepcopy(X)
x.sort()
mid_min = x[N//2-1]
mid_max = x[N//2]

for i in range(N):
    if X[i] <= mid_min:
        print(mid_max)

    else:
        print(mid_min)
