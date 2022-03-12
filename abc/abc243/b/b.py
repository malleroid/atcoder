N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = 0
for i in range(N):
    if A[i] == B[i]:
        ans1 += 1

set_a = set(A)
set_b = set(B)

common_attr = set_a & set_b
common_num = len(common_attr)

ans2 = common_num-ans1

print(ans1, ans2, sep='\n')
