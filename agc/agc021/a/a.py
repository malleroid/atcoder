N = input()

s = N[0]+'9'*(len(N)-1)

if int(s) <= int(N):
    ans = sum(list(map(int, str(s))))
    print(ans)

else:
    ans = int(N[0])-1+9*(len(N)-1)
    print(ans)
