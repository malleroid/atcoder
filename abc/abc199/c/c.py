N = int(input())
S = list(input())
Q = int(input())

left = S[:N]
right = S[N:]

for i in range(Q):
    T, A, B = map(int, input().split())

    A -= 1
    B -= 1

    if T == 1:

        if A < N and B < N:
            left[A], left[B] = left[B], left[A]

        elif A < N and N <= B:
            left[A], right[B-N] = right[B-N], left[A]

        else:
            right[A-N], right[B-N] = right[B-N], right[A-N]

    else:
        left, right = right, left

print(''.join(left+right))
