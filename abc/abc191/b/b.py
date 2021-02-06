N, X = map(int, input().split())
A = list(map(int, input().split()))

A_rem = [str(i) for i in A if i != X]

a = ' '.join(A_rem)

print(a)
