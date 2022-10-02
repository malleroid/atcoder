N = int(input())
A = list(map(int, input().split()))

n = len([i for i in A if i < 0])

abs_A = [abs(i) for i in A]
abs_A.sort()

if n % 2 == 1:
    ans = sum(abs_A)-2*abs_A[0]

else:
    ans = sum(abs_A)

print(ans)
