S = input()
K = int(input())

if len(set(S)) == 1:
    print(len(S)*K//2)

else:

    now = 1
    s = []

    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            now += 1

            if i == len(S)-2:
                s.append(now)

        else:
            s.append(now)
            now = 1

    ans = 0
    if S[0] == S[-1]:
        ans += (s[0]+s[-1])//2*(K-1)

        ans += s[0]//2
        ans += s[-1]//2

        s.pop(0)
        s.pop(-1)

        for i in range(len(s)):
            ans += s[i]//2*K

    else:
        for i in range(len(s)):
            ans += s[i]//2*K

    print(ans)
