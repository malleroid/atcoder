N = int(input())

n_1 = 0
n_1s = ''
n_2 = 0
n_2s = ''

for i in range(N):
    S, T = input().split()
    T = int(T)

    if T > n_1:
        n_2 = n_1
        n_2s = n_1s

        n_1 = T
        n_1s = S

    elif T > n_2:
        n_2 = T
        n_2s = S

print(n_2s)
