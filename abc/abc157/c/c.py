N, M = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(M)]

before = 10**(N-1) if N >= 2 else 0
after = 10**N

for i in range(before, after):
    s = str(i)
    fl = True
    for j in range(M):

        if int(s[sc[j][0]-1]) != sc[j][1]:
            fl = False
            break

    if fl is True:
        print(i)
        exit()

print(-1)
