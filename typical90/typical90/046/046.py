N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cnt = 46

for i in range(N):
    A[i] = A[i] % 46
    B[i] = B[i] % 46
    C[i] = C[i] % 46

a = [0]*cnt
b = [0]*cnt
c = [0]*cnt

for i in range(N):
    a[A[i]] += 1
    b[B[i]] += 1
    c[C[i]] += 1

ans = 0
for i in range(cnt):
    for j in range(cnt):
        for k in range(cnt):

            if (i+j+k) % cnt == 0:
                ans += a[i]*b[j]*c[k]

print(ans)
