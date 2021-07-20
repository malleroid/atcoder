N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A, B = [list(i) for i in zip(*AB)]

A.reverse()
B.reverse()

ans = 0

for i in range(N):
    num = (A[i]+(ans % B[i])) % B[i]

    if num != 0:
        num = B[i]-num

    ans += num

print(ans)
