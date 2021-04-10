O = list(input())
E = list(input())

ans = ''
for i in range(len(O)):

    if len(E) != 0:
        ans += O[0]+E[0]
        O.pop(0)
        E.pop(0)
    else:
        ans += O[0]
        O.pop(0)

print(ans)
