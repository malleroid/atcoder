N, A, B = map(int, input().split())

ans = [[""]*(B*N) for _ in range(A*N)]

n = 0
for i in range(A*N):
    ln = i//A

    for j in range(B*N):
        cn = j//B

        n = ln+cn
        ans[i][j] = "." if n % 2 == 0 else "#"

print("\n".join("".join(line) for line in ans))
