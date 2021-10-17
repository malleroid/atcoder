N, M = map(int, input().split())

lock = {i: [] for i in range(1, N+1)}
n = {i: i for i in range(1, N+1)}

# print(lock)
# exit()
for i in range(M):
    A, B = map(int, input().split())

    if B in lock[A]:
        print(-1)
        exit()

    else:
        lock[A].append(B)

        if A > B:
            n[A], n[B] = n[B], n[A]

n = list(n).sort(key=lambda x: x[1])
print(n)
