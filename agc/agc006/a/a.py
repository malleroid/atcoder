N = int(input())
s = input()
t = input()

n = 0
for i in range(1, N+1):

    s2 = s[-i:]

    if s2 in t:
        n = i

ans = 2*N-n
print(ans)
