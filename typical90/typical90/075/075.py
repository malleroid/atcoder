import copy

N = int(input())

A = [N]
ans = 0

while len(A) > 0:

    B = []
    for v in A:

        i = 1
        p = 1
        while i*i <= v:
            if v % i == 0:
                p = i

            i += 1

        if p != 1:
            B.append(p)
            B.append(v//p)

    A = copy.deepcopy(B)
    if len(A) > 0:
        ans += 1

print(ans)
