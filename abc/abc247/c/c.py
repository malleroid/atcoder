N = int(input())

S = ['']*N
S[0] = '1'

for i in range(1, N):
    S[i] = " ".join([S[i-1], str(i+1), S[i-1]])

print(S[N-1])
