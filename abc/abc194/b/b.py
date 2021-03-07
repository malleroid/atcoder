N = int(input())
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

a = min(A)
b = min(B)
a_index = A.index(a)
b_index = B.index(b)

if a_index == b_index:
    s = a+b

    rem_A = A[:]
    rem_A.pop(b_index)
    rem_a = min(rem_A)
    s = min(s, max(rem_a, b))

    rem_B = B[:]
    rem_B.pop(a_index)
    rem_b = min(rem_B)
    s = min(s, max(a, rem_b))

    print(s)

else:
    print(max(a, b))
