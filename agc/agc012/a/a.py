N = int(input())
a = list(map(int, input().split()))

a.sort()

a_n = a[N:]

a_2n = [b for i, b in enumerate(a_n) if i % 2 == 0]

print(sum(a_2n))
