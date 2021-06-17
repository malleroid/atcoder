import itertools

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [list(map(int, input().split())) for _ in range(M)]

L = [i for i in range(N)]

pair = [[True]*N for _ in range(N)]

for v in XY:
    pair[v[0]-1][v[1]-1] = False
    pair[v[1]-1][v[0]-1] = False


ans = pow(10, 5)
for v in itertools.permutations(L):

    flag = True
    num = 0
    for i in range(len(v)):

        if i != len(v)-1 and pair[v[i]][v[i+1]] is False:
            flag = False
            break

        else:
            num += A[v[i]][i]

    if flag is True:
        ans = min(ans, num)


print(ans if ans != pow(10, 5) else '-1')
