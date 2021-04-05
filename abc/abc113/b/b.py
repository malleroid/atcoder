N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

ans = 0
diff = 10**5
for i, h in enumerate(H):
    if abs(A-(T-0.006*h)) < diff:
        diff = abs(A-(T-0.006*h))
        ans = i+1

print(ans)
