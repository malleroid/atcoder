A, B, C = map(int, input().split())

if A == B or (abs(A) == abs(B) and C % 2 == 0):
    print('=')

elif A > B:
    if B >= 0:
        print('>')

    elif A < 0:
        print('<' if C % 2 == 0 else '>')

    else:
        if abs(A) > abs(B):
            print('>')
        else:
            print('<' if C % 2 == 0 else '>')

else:
    if A >= 0:
        print('<')

    elif B < 0:
        print('>' if C % 2 == 0 else '<')

    else:
        if abs(A) > abs(B):
            print('>' if C % 2 == 0 else '<')
        else:
            print('<')
