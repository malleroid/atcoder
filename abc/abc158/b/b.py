N, A, B = map(int, input().split())

num = N//(A+B)
mod = N % (A+B)

ans = A*num

if mod <= A:
    ans += mod

else:
    ans += A

print(ans)
