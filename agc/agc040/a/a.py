S = input()

t = [0 for _ in range(len(S)+1)]

for i in range(len(S)):

    if S[i] == '<':

        t[i+1] = t[i]+1


for i in range(len(S)-1, -1, -1):

    if S[i] == '>':

        t[i] = max(t[i], t[i+1]+1)

ans = sum(t)

print(ans)
