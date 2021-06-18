# 数式変換, 因数分解, 等価置換
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 1
for v in A:
    s = sum(v)
    ans *= s
    ans %= (pow(10, 9)+7)

print(ans)
