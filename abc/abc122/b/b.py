S = input()
acgt = ['A', 'C', 'G', 'T']

ans = 0
num = 0
for s in S:
    if s in acgt:
        num += 1
    else:
        num = 0

    ans = max(ans, num)

print(ans)
