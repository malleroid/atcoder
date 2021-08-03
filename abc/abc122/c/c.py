N, Q = map(int, input().split())
S = input()

ac = [0]*N
num = 0
for i in range(N-1):
    if S[i] == 'A' and S[i+1] == 'C':
        num += 1
    ac[i+1] = num

for i in range(Q):
    left, right = map(int, input().split())
    left -= 1
    right -= 1

    print(ac[right]-ac[left])
