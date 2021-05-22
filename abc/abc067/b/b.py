N, K = map(int, input().split())
l = list(map(int, input().split()))

l.sort(reverse=True)

l2 = l[:K]

print(sum(l2))
