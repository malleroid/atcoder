V, A, B, C = map(int, input().split())

mod = V % (A+B+C)

if mod < A:
    print('F')

elif mod < A+B:
    print('M')

else:
    print('T')
