# データ構造(mapやqueueも参考に)

N = int(input())

s = set()

for i in range(N):

    S = input()
    if S not in s:
        s.add(S)
        print(i+1)
