S = input()
K = int(input())

for i in range(len(S)):

    if S[i] == '1' and i+1 == K:
        print(1)
        exit()

    elif int(S[i]) >= 2:
        print(S[i])
        exit()
