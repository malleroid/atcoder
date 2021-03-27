A, B, K = map(int, input().split())

a = set()

if B-A <= K:
    for i in range(B-A+1):
        a.add(A+i)

else:
    for i in range(K):
        a.add(A+i)
        a.add(B-i)

ans = list(a)
ans.sort()
print(*ans, sep='\n')
