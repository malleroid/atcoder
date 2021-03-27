A = input()
B = input()

if A == B:
    print('EQUAL')

elif len(A) > len(B):
    print('GREATER')

elif len(A) < len(B):
    print('LESS')

else:
    for i in range(len(A)):
        if A[i] > B[i]:
            print('GREATER')
            exit()
        elif A[i] < B[i]:
            print('LESS')
            exit()
