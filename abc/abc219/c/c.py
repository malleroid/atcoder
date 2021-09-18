X = input()
N = int(input())
S = [input() for _ in range(N)]


def neo_ord(s):
    n = []
    for c in s:
        p = X.index(c)
        n.append(p)

    return n


S.sort(key=lambda x: neo_ord(x))
print(*S, sep='\n')
